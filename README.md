# IFSC Validator

IFSC validator is a python library that validates IFSC bank codes by making use of razorpay API.

## Installation

* Make sure you have <span style="font-size:larger;">[python3](https://www.python.org/downloads/) </span> installed in your system
* Clone the repository and cd into `ifsc`
    ``` bash 
        git clone https://github.com/rahulkaliyath/ifsc.git
        cd ifsc 
     ```
* ``` python
    pip install -r requirements.txt
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

