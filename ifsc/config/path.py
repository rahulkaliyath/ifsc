from pkg_resources import resource_filename

BASE_URL = 'https://ifsc.razorpay.com/'
ASSETS_PATH = resource_filename("ifsc", "assets/") 
IFSC_PATH = resource_filename("ifsc", "assets/IFSC.json")
BANK_NAMES_PATH = resource_filename("ifsc", "assets/bank_names.json")
BANK_DETAILS_PATH = resource_filename("ifsc", "assets/banks.json")
