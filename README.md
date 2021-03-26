# IFSC Validator

IFSC validator is a python library that validates IFSC bank codes by making use of razorpay API.

## Installation

* Make sure you have <span style="font-size:larger;">[python3](https://www.python.org/downloads/) </span> installed in your system
* Clone the repository and cd into `ifsc`
    ```bash 
    git clone https://github.com/rahulkaliyath/ifsc.git
    cd ifsc 
    ```
* ``` python
  pip install -r requirements.txt
  ```
* Install the library by running
  ``` python
  pip install .
  ```
* Verify Installation by running the following in terminal
  ```bash 
  pip freeze | grep ifsc 
  ``` 
  `Output`
  ```bash
  ifsc-validator==1.0.0
  ```


## Global Import Set Up

To import the IFSC module from any directory, save the `ifsc` directory path in `PYTHONPATH` Environment Variable.

### Setting PYTHONPATH in Mac/Linux

* Open Terminal
* ```bash
  echo "export PYTHONPATH= $PYTHONPATH:<Absolute-file-path-of-ifsc-directory>" >> ~/.bash_profile
  ```

### Setting PYTHONPATH in Windows

* Open Git Bash Terminal
* ```bash
  export PYTHONPATH="$PYTHONPATH:<Absolute-file-path-of-ifsc-directory>"
  ```

**Note: The above command will only work on one shell and the PATH is cleared when shell is closed ** 

To make the PYTHONPATH persistent, do the following steps

* Right Click on `This PC` and select `properties`
* Click on `Advanced System Settings`
* Under `Advanced` tab, click on `Environment Variables...` button
* Select `new` in the `user variable` section
* Give `Variable Name` as `PYTHONPATH` and `ifsc` absolute path as `Variable Value`

## Usage

Once the package is installed, the library can be accessed through CLI or by importing in other modules.

### Command Line Usage
`ifsc-cli` is the command to access the library.
#### Options
`-ifsc` , `-i` : To validate and get information on an `IFSC` code

`-bank` , `-b` : To validate and get information on a `BANK` code

`-city` , `-c` : Used along with `-bank` to get list of given bank in given city

`--validate` , `-v` : To validate an `IFSC` code or a `BANK` code

`--get` , `-g` : To get information of an `IFSC` code or a `BANK` code

`--head` , `-H` : List only top `n` results

`--help` , `-h` : To view all the options and usage of each option


### Examples
##### IFSC Code Validate
```bash
ifsc-cli -ifsc HDFC0CAACOB --validate
```
##### Output
  ```
  True
  ```

##### Get Details of an IFSC Code
```bash
ifsc-cli -ifsc HDFC0CAACOB --get
```
##### Output
  ```
+--------------------------------------------------------+
|                      Bank Details                      |
+----------+---------------------------------------------+
|   Name   |                    Values                   |
+----------+---------------------------------------------+
|  BRANCH  |         Akhand Anand Co.op Bank IMPS        |
|  CENTRE  |                    SURAT                    |
| DISTRICT |                    SURAT                    |
|  STATE   |                   GUJARAT                   |
| ADDRESS  | NEAR ANATH BALASHRAM, KATARGAM SURAT.395004 |
| CONTACT  |                   2536772                   |
|   IMPS   |                     True                    |
|   CITY   |                    SURAT                    |
|   UPI    |                     True                    |
|   MICR   |                  395002437                  |
|   RTGS   |                     True                    |
|   NEFT   |                     True                    |
|  SWIFT   |                   HDFCINBB                  |
|   BANK   |           Akhand Anand Co.op Bank           |
| BANKCODE |                     AACX                    |
|   IFSC   |                 HDFC0CAACOB                 |
+----------+---------------------------------------------+
  ```
##### Bank Code Validate
```bash
ifsc-cli -bank HDFC --validate
```
##### Output
  ```
  True
  ```

##### Get Details of a Bank Code
```bash
ifsc-cli -bank HDFC --get
```
##### Output
  ```
+--------------------------+
|       Bank Details       |
+------------+-------------+
|    Name    |    Values   |
+------------+-------------+
|    code    |     HDFC    |
|    type    |   Private   |
|    ifsc    | HDFC0999999 |
|    micr    |  400240001  |
|    iin     |    607152   |
|    apbs    |     True    |
| ach_credit |     True    |
| ach_debit  |     True    |
| nach_debit |     True    |
|    upi     |     True    |
|    name    |  HDFC Bank  |
+------------+-------------+
  ```

##### Get list of banks in given city
```bash
ifsc-cli -city bangalore -bank HDFC --head 2
```
##### Output
```
+------------------------------------------------------------------------------------------------------------+
|                                                Bank Details                                                |
+-----------+-------------+----------------------------------------------------------------------------------+
| Bank Name |     IFSC    |                                     Address                                      |
+-----------+-------------+----------------------------------------------------------------------------------+
| HDFC BANK | HDFC0000009 |          24/3 HDFC HOUSE,NO. 51 KASTURBA ROAD,BANGALOREKARNATAKA560 001          |
| HDFC BANK | HDFC0000041 | NO.47, MARGOSA ROAD,NEXT TO BSNL OFFICE, 15TH CROSS,MALLESHWARAM,  BANGALORE,KAR |
+-----------+-------------+----------------------------------------------------------------------------------+
```
### Testing
The test cases are written in `test/test_ifsc.py`.CD into `ifsc` root directory and Run the following to test the library
``` bash
pytest .
```