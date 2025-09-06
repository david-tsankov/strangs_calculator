# How to install 
This is for UNIX systems, and does not apply to windows

## Cloning the repository in a folder
1. Create a folder (directory) in which you will clone the repository
2. Go into the repository through the terminal then run  
"git clone https://github.com/david-tsankov/strangs_calculator.git"

## Creating a virtual environment and installing dependencies
Before installing it would be best to create a virtual environment and install all the packages in requirements.txt  
This can be done in 2 ways:
### Using pyenv:
1. Go into the directory in which you cloned the repository, then go into the folder of the repo itself by "cd strangs_calculator"
2. Before creating a virtual environment you want to make sure you have python 3.13.5 in pyenv
3. Run "pyenv virtualenv 3.13.5 venv_strang", where 'venv_strang' can be substituted by whatever name you want to give to your environment
4. After creating the environment you want to activate it by running "pyenv activate venv_strang", once again you can substitute the name of the environment
5. After activating the environment you need to install the dependencies by running  
"pip install -r requirements.txt"  
NOTE: You need to be in "strangs_calculator" directory, not the name of the folder in which you cloned the repo, as "requirements.txt" is in the repo folder itself

## Running the program
After installing all the dependencies, and having activated your virtual environment you can either:
1. Run "python app.py" in the terminal or
2. Open the folder in vscode and run the file from there

For information on how to use the program check the documentation


## Below are videos showing how to install the calc step by step as written here:

[Installation Guide](https://github.com/user-attachments/assets/7d5689ea-a211-4b25-a9e1-2d436d90970e)

[sample_use.webm](https://github.com/user-attachments/assets/8da72edd-ab65-4deb-993e-52fb1d286013)
