Installation
*************

Setup
#####

1 Make sure you have python3 installed in your system

2 Clone the repository and cd into **ifsc**::

    git clone https://github.com/rahulkaliyath/ifsc.git

3 Run :: 

    pip install -r requirements.txt

4 Install the library by running ::

  pip install .

5 Verify Installation by running the following in terminal ::
  
  pip freeze | grep ifsc 

**Output** ::

  ifsc-validator==1.0.0



Global Import Set Up [Optional]
##############################
If you do not want to install the libray and want to import the IFSC module from any directory, save the **ifsc** directory path in **PYTHONPATH** Environment Variable.

Setting PYTHONPATH in Mac/Linux
###############################

* Open Terminal
* Run ::

    echo "export PYTHONPATH= $PYTHONPATH:<Absolute-file-path-of-ifsc-directory>" >> ~/.bash_profile

Setting PYTHONPATH in Windows
#############################

* Open Git Bash Terminal
* Run ::

    export PYTHONPATH="$PYTHONPATH:<Absolute-file-path-of-ifsc-directory>"

**Note: The above command will only work on one shell and the PATH is cleared when shell is closed ** 

To make the PYTHONPATH persistent, do the following steps

* Right Click on **This PC** and select **properties**
* Click on **Advanced System Settings**
* Under **Advanced** tab, click on **Environment Variables...** button
* Select **new** in the **user variable** section
* Give **Variable Name** as **PYTHONPATH** and **ifsc** absolute path as **Variable Value**