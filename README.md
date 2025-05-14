# Python_DLMDSPWP01
This Project is developed for my university course purpose "Programming with Python"

# 🚀Run this project:

## 1) Clone this project to your local using the below git command 
    ```bash
    git clone https://github.com/Sanjeevkapoor421/Sanjeev_python_DLMDSPWP01.git
    cd Sanjeev_python_DLMDSPWP01
    ```
## 2) Do git checkout to developement_branch
    ```bash
    git checkout features/develope_branch
    ```
## 3) Setting up the virtual environment and running the project
    ```bash
    make all
    ``` 
This will :
 * create a virtual environment " myenv "
 * It will install the required dependencies from requirements file
 * Lastly it will run the pipeline script src_sanjeev/main.py file

# 🛠️ Manually run this project if the above ' make ' command didn't work
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
    python src_sanjeev/main.py
    ```