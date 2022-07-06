from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def prepare_callbacks(source_download_dir, local_data_dir):
    pass




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage three started")
        prepare_callbacks(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info("stage three completed! callbcks are prepared and save as a binary>>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e