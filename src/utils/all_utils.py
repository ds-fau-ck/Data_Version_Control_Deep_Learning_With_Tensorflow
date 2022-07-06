import yaml
import os
import json
import logging
import time

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content
    
def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"directory is created at {dir_path}")
def get_timestamp(name):
    timestamp=time.asctime().replace(" ","_").replace(":","_")
    unique_name=f"{name}_at_{timestamp}"
    return unique_name