import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/Data_ingestion.py",
    f"src/{project_name}/components/Data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/piplines/__init__.py",
    f"src/{project_name}/piplines/training_piplines.py",
    f"src/{project_name}/piplines/prediction_piplines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":                               #this create file
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:                                            # exit if file is already exist
        logging.info(f"{filename} is already exist")