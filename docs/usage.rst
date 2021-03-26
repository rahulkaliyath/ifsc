Usage
*****

Once the package is installed, the library can be accessed through CLI or by importing in other modules.

Command Line Usage
##################

**ifsc-cli** is the command to access the library.
#### Options
**-ifsc** , **-i** : To validate and get information on an **IFSC** code

**-bank** , **-b** : To validate and get information on a **BANK** code

**-city** , **-c** : Used along with **-bank** to get list of given bank in given city

**--validate** , **-v** : To validate an **IFSC** code or a **BANK** code

**--get** , **-g** : To get information of an **IFSC** code or a **BANK** code

**--head** , **-H** : List only top **n** results

**--help** , **-h** : To view all the options and usage of each option


Examples

- IFSC Code Validate ::

      ifsc-cli -ifsc HDFC0CAACOB --validate




- Get Details of an IFSC Code ::

      ifsc-cli -ifsc HDFC0CAACOB --get


- Bank Code Validate ::

      ifsc-cli -bank HDFC --validate

- Get Details of a Bank Code ::

      ifsc-cli -bank HDFC --get
  

- Get list of banks in given city ::

      ifsc-cli -city bangalore -bank HDFC --head 2

Testing
*******
The test cases are written in **test/test_ifsc.py**.CD into **ifsc** root directory and Run the following to test the library ::

    pytest .  
