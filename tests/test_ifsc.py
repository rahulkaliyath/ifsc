from ifsc.utils import test_utils
from ifsc.ifsc import IFSC
import pytest
from ifsc.utils.custom_exception import InvalidCode


ifsc = IFSC()

def test_validate():
    assert ifsc.validate("HDFC0CAACOB") == True
    assert ifsc.validate("HDFC03AACO3") == False

def test_fetch_details():
    assert ifsc.fetch_details("HDFC0CADIBK") == test_utils.fetch_details_1
    with pytest.raises(InvalidCode):
            ifsc.fetch_details("HDFS5CADIBK")

def test_validate_bank():
    assert ifsc.validate_bank("HDFC") == True
    assert ifsc.validate_bank("HIFC") == False
    assert ifsc.validate_bank("HIFCJH",from_get=True) == (False,[],"")


def test_get_bank_name():
    assert ifsc.get_bank_name("HDFC") == "HDFC Bank"
    with pytest.raises(InvalidCode):
        ifsc.get_bank_name("HDYTY")
