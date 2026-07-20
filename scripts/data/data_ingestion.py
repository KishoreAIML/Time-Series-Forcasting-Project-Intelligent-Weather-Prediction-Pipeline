#import neccesory libraries
import os
import pandas as pd
import time

from memory_profiler import profile # for printing the memory usage if the function

import traceback
import logging

from urllib.parse import urlparse
import kaggle

from src.utils.config import ROOT_DIR,RAW_DATA

import warnings
warnings.filterwarnings("ignore") #to ignore warnings throught the script

#defining log file
current_loc = os.getcwd()
try:
    os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Intelligent_Weather_Prediction_Pipeline/scripts/data/logs")
except Exception as e:
    print("faild!")
    traceback.print_exc()

file_name = os.path.basename(__file__)
file_name = file_name.split(".")
logging.basicConfig(
    filename= f"{file_name[0]} logfile.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s",
    level = logging.DEBUG
)

logging.info("Reading dataset file...")

#method for reading dataset with filename perameter
@profile
def load_data(filename,filelocation):
    """
    Collects Weather data of Delhi for weather forcasting pipeline

    Args:
        filename(String): Name of the file
        filelocation(String): file location in local machine

    Returns:
        Dataset(DataFrame): it contains past 5 Years delhi weather recors and variables
    
    """
    os.chdir(filelocation)
    try:
        start = time.time()
        dataset = pd.read_csv(f"{filename}.csv")
        end = time.time()
        print(f"loading time {round(end-start,2)}secs")
    except Exception as e:
        print("faild!")
        traceback.print_exc()
    return dataset

logging.info("dataset loaded successfully")

@profile
def download_house_list_data(url):
    """
    downloads dataset from kaggle data scourse by using url of the dataset file in website.

    Args:
        url (String): web site url for dataset.

    Returns:
        Saves downloaded file in location.
    
    """
    logging.info("creating dataset ID...")
    parsed = urlparse(url).path.strip("/").split("/")
    dataset_id = f"{parsed[1]}/{parsed[2]}"
    logging.info("dataset ID Created")

    dataset = kaggle.api.dataset_download_files(
        dataset = dataset_id,
        path = ROOT_DIR/RAW_DATA,
        unzip = True
    )

    print("dataset downloaded Successfully!")

@profile
def read_data():
    """
    Reads the downloaded dataset file from dataset location.

    Args:
        Nothing

    Returns:
        Dataset(DataFrame): it contains Lahore House Listings from Zameen.com (2025).
    """
    dataset = pd.read_csv(ROOT_DIR/RAW_DATA / "lahore_house_listings_zameen.csv")
    return dataset



