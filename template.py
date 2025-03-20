import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s')

project_name = 'Brain-Tumor-Classification'

#list of files/folders that needs to be in my project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    path = Path(filepath)
    #separate folders and files
    filedir , filename = os.path.split(path)

    #create folders
    if filedir:
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Folder created: {filedir}")

    #create files
    if (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path, 'w') as f:
            pass
            logging.info(f"Empty File created: {path}")

    else:
        logging.info(f"File already exists: {path}")