from utils import test_utils
from ifsc import IFSC

ifsc = IFSC()

print(ifsc.get_bank_name("HDFC"))

def test_validate():
    assert ifsc.validate("HDFC0CAACOB") == True
    assert ifsc.validate("HDFC03AACO3") == False

def test_fetch_details():
    assert ifsc.fetch_details("HDFC0CADIBK") == test_utils.fetch_details_1
    assert ifsc.fetch_details("HDFS5CADIBK") == "Invalid IFSC"
