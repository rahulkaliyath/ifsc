from config import path
from utils import io_operation,print_table
from utils.custom_exception import InvalidCode
import requests
import sys
import argparse
import os

module_path = os.environ['PYTHONPATH']

URL=path.BASE_URL
ASSETS_PATH = path.ASSETS_PATH
IFSC_PATH =  path.IFSC_PATH
BANK_NAMES_PATH =  path.BANK_NAMES_PATH
BANK_DETAILS_PATH =  path.BANK_DETAILS_PATH

class IFSC:
    """
    Class for Validating IFSC Codes
    """

    def __init__(self):
        '''Initializing the IFSC Class'''

    #Function to validate given IFSC code
    def validate(self,ifsc):
        '''
        Function to validate given IFSC code 

        Args:
            ifsc: IFSC code to validate

        Returns:
            True if valid, False otherwise.

        Usage: 
           >>> validate("HDFC0CAACOB")
           >>> True

           >>> validate("HDFC0CAASBHB")
           >>> False

        '''

        #Checking if given code meets the IFSC Code Standard
        if len(ifsc) != 11 or ifsc[4] != '0':
            return False

        bank_code = ifsc[:4].upper()
        branch_code = ifsc[5:].upper()

        ifsc_list = io_operation.load_json(IFSC_PATH)

        if bank_code not in ifsc_list.keys():
            return False

        bank_branch_codes = ifsc_list[bank_code]
        
        if branch_code.isdigit():
            return int(branch_code) in bank_branch_codes
        
        return branch_code in bank_branch_codes

    #Function to fetch details of the bank from given IFSC code
    def fetch_details(self,ifsc):
        '''
        Function to fetch details of the bank from given IFSC code

        Args:
            ifsc: IFSC code 

        Returns:
            JSON object of bank details if  IFSC is valid, "Invalid IFSC" otherwise.

        Usage: 
           >>> fetch_details("HDFC0CAACOB")
           >>> {
                'RTGS': True, 
                'NEFT': True,
                'CENTRE': 'XYZ', 
                'CITY': 'XYZ', 'IMPS': True,
                 ...
                'STATE': 'XYZ'
                }

           >>> fetch_details("HDFC0CHGYB")
           >>> InvalidCode("Invalid IFSC Code")

        '''
        #Raise an Exception if the IFSC code is not valid
        if not self.validate(ifsc):
            raise InvalidCode("Invalid IFSC Code")
        
        api_endpoint = URL + ifsc

        #Fetch details from Razorpay API
        bank_details = requests.get(api_endpoint).json()

        return bank_details

    #Function to validate given Bank code
    def validate_bank(self,bank_code,from_get=False):
        ''' 
        Function to validate given Bank code 

        Args:
            bank_code: Bank code to validate
            from_get: To identify whether the function is called from another function for validation

        Returns:
            True if valid, False otherwise.

            ** When from_get is set:

                returns (True, bank_names , bank_code) if valide, otherwise (False, [], "")


        Usage: 
           >>> validate_bank("HDFC")
           >>> True

           >>> validate_bank("HVSTV")
           >>> False

           >>> validate_bank("HDFC", from_get=True)
           >>> (True, {<bank_names>} , bank_code)

           >>> validate_bank("HDFC", from_get=True)
           >>> (False, [] , "")

        '''


        if len(bank_code) != 4:
            #Returning to another caller function
            if from_get:
                return False, [], ""  
            return False
        
        bank_code = bank_code.upper()

        bank_names = io_operation.load_json(BANK_NAMES_PATH)

        validity = bank_code in bank_names.keys()

        #Returning to another caller function
        if from_get:
            return validity, bank_names , bank_code

        return validity
        
    #Function to get bank name for the given Bank code 
    def get_bank_name(self,bank_code):
        '''
        Function to get bank name for the given Bank code 

        Args:
            bank_code: Bank code to validate

        Returns:
            Bank Name if valid, "INVALID BANK CODE" otherwise.

        Usage: 
           >>> get_bank_name("HDFC")
           >>> HDFC Bank

           >>> get_bank_name("HDY&")
           >>> InvalidCode("Invalid Bank Code")

        '''

        
        validity, bank_names, bank_code = self.validate_bank(bank_code,from_get=True)

        if validity:
            return bank_names[bank_code]
        
        #Raise an Exception if the Bank code is invalid
        raise InvalidCode("Invalid Bank Code")

    # Function to get bank details for the given Bank code
    def get_details(self,bank_code):
        '''
        Function to get bank details for the given Bank code 

        Args:
            bank_code: Bank code to validate

        Returns:
            JSON object of bank details if valid bank code, nvalidCode("Invalid Bank Code") otherwise

        Usage: 
           >>> get_details("HDFC")
           >>> {
                code : "HDFC" 
                type : 'Private' 
                ifsc : 'XYZS0HGFK5' 
                ...
                upi : 'XYZ51151' 
                name : 'XYZ'
                }

           >>> get_details("HDY&")
           >>> InvalidCode("Invalid BANK Code")

        '''

        validity, bank_names, bank_code = self.validate_bank(bank_code,from_get=True)

        if validity:
            all_bank_details = io_operation.load_json(BANK_DETAILS_PATH)

            bank_details = all_bank_details[bank_code]
            bank_details['name'] = bank_names[bank_code]

            return bank_details
        
        #Raise an Exception if the Bank code is invalid
        raise InvalidCode("Invalid Bank Code")

    def get_banks_in_city(self,bank,city,head=-1):
        '''
        Function to get list bank details for the given Bank code in the given city

        Args:
            bank_code: Bank code to validate

        Returns:
            JSON object of bank details in a given city if valid bank code, "INVALID BANK CODE" otherwise

        Usage: 
           >>> get_banks_in_city("SBIN","chennai)
           >>> [{'IFSC': 'SBIN0000249', 
                'BRANCH': 'TRIPLICANE (CHENNAI)', 
                'CENTRE': 'CHENNAI', 'STATE': 'TAMIL NADU', 
                ...
                'BANK': 'STATE BANK OF INDIA'},
                ...
                ]

           >>> get_banks_in_city("SBIJU","chennai)
           >>> InvalidCode("Invalid BANK Code")

        '''
        validity, bank_names, bank_code = self.validate_bank(bank,from_get=True)

        if not validity:
            raise InvalidCode("Invalid Bank Code")
        
        banks = io_operation.load_json(ASSETS_PATH + f"{bank}.json")

        return [bank for bank in banks if bank['CITY'] == city.upper()][:head]

def main():
    ifsc = IFSC()
    parser = argparse.ArgumentParser()
    parser.add_argument("-ifsc","-i", help="Enter the IFSC CODE")
    parser.add_argument("-bank","-b", help="Enter the Bank CODE")
    parser.add_argument("-city","-c", help="Enter the name of the city ")
    parser.add_argument("-v","--validate",action="store_true", help="Use flag to validate code")
    parser.add_argument("-g","--get",action="store_true", help="Use flag to get details")
    parser.add_argument("-H","--head",type=int, help="Use flag to list only top n results")



    args = parser.parse_args()

    ifsc_code = args.ifsc
    bank = args.bank
    city = args.city
    validate = args.validate
    get = args.get
    head = args.head

    if ifsc_code and validate:
        print(ifsc.validate(ifsc_code))
    
    elif ifsc_code and get:
        data = ifsc.fetch_details(ifsc_code)
        print_table.table(data)

    elif bank and validate:
        print(ifsc.validate_bank(bank))

    elif bank and get:
        data = ifsc.get_details(bank)
        print_table.table(data)

    elif city and bank:
        head = head if head else -1 
        data = ifsc.get_banks_in_city(bank,city,head)
        print_table.table_row(data)
    
    else:
        raise InvalidCode("Invalid Arguments Passed. Run ifsc-cli --help to view usages")




if __name__ == "__main__":
    main()

# ifsc = IFSC()

# ifsc.get_banks_in_city("HDFC","CHENNAI")

# print(ifsc.validate("HDFC0CAACOB"))

# print(ifsc.fetch_details("HDFC0CADIBK"))
# print(ifsc.validate_bank("HDFC",from_get=True))
# print(ifsc.get_bank_name("YESB"))
# print(ifsc.get_details("kkbk"))


