from config import path
from utils import io_operation
import requests
import sys
import argparse
import os

module_path = os.environ['PYTHONPATH']

URL=path.BASE_URL
IFSC_PATH = module_path + path.IFSC_PATH
BANK_NAMES_PATH = module_path + path.BANK_NAMES_PATH
BANK_DETAILS_PATH = module_path + path.BANK_DETAILS_PATH

class IFSC:
    """
    Class for Validating IFSC Codes
    """

    def __init__(self):
        '''Initializing the IFSC Class'''

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
           >>> "Invalid IFSC"

        '''

        if not self.validate(ifsc):
            return "Invalid IFSC"
        
        api_endpoint = URL + ifsc

        bank_details = requests.get(api_endpoint).json()

        return bank_details

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
            if from_get:
                return False, [], ""
            return False
        
        bank_code = bank_code.upper()

        bank_names = io_operation.load_json(BANK_NAMES_PATH)

        validity = bank_code in bank_names.keys()

        if from_get:
            return validity, bank_names , bank_code

        return validity
        

    def get_bank_name(self,bank_code):
        '''
        Function to get bank name for the given Bank code 

        Args:
            bank_code: Bank code to validate

        Returns:
            True if valid, False otherwise.

        Usage: 
           >>> get_bank_name("HDFC")
           >>> HDFC Bank

           >>> get_bank_name("HDY&")
           >>> "INVALID BANK CODE"

        '''

        
        validity, bank_names, bank_code = self.validate_bank(bank_code,from_get=True)

        if validity:
            return bank_names[bank_code]
        
        return "INVALID BANK CODE"


    def get_details(self,bank_code):
        '''
        Function to get bank details for the given Bank code 

        Args:
            bank_code: Bank code to validate

        Returns:
            JSON object of bank details if valid bank code, "INVALID BANK CODE" otherwise

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
           >>> "INVALID BANK CODE"

        '''

        validity, bank_names, bank_code = self.validate_bank(bank_code,from_get=True)

        if validity:
            all_bank_details = io_operation.load_json(BANK_DETAILS_PATH)

            bank_details = all_bank_details[bank_code]
            bank_details['name'] = bank_names[bank_code]

            return bank_details
        
        return "INVALID BANK CODE"


def main():
    pass


if __name__ == "__main__":
    main()

ifsc = IFSC()

# print(ifsc.validate("HDFC0CAACOB"))

print(ifsc.fetch_details("HDFC0CADIBK"))

# print(ifsc.get_bank_name("YESB"))
# print(ifsc.get_details("kkbk"))

