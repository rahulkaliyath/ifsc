from config import config
from utils import io_operation
import requests

URL=config.BASE_URL
IFSC_PATH = config.IFSC_PATH
BANK_NAMES_PATH = config.BANK_NAMES_PATH
BANK_DETAILS_PATH = config.BANK_DETAILS_PATH

def validate(ifsc):

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

    
def fetch_details(ifsc):

    if not validate(ifsc):
        return "Invalid IFSC"
    
    api_endpoint = URL + ifsc

    bank_details = requests.get(api_endpoint).json()

    return bank_details

def validate_bank(bank_code,from_get_name=False):

    if len(bank_code) != 4:
        if from_get_name:
            return False, [], ""
        return False
    
    bank_code = bank_code.upper()

    bank_names = io_operation.load_json(BANK_NAMES_PATH)

    validity = bank_code in bank_names.keys()

    if from_get_name:
        return validity, bank_names , bank_code

    return validity
    

def get_bank_name(bank_code):
    
    validity, bank_names, bank_code = validate_bank(bank_code,from_get_name=True)

    if validity:
        return bank_names[bank_code]
    
    return "INVALID BANK CODE"


def get_details(bank_code):

    validity, bank_names, bank_code = validate_bank(bank_code,from_get_name=True)

    if validity:
        all_bank_details = io_operation.load_json(BANK_DETAILS_PATH)

        bank_details = all_bank_details[bank_code]
        bank_details['name'] = bank_names[bank_code]

        return bank_details
    
    return "INVALID BANK CODE"




print(validate("HDFC0CAACOB"))

# print(fetch_details("HDFC0CADIBK"))

print(get_bank_name("YESB"))
print(get_details("kkbk"))


    
