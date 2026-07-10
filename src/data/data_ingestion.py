#import neccesory libraries
import os
import pandas as pd
import time
import traceback
import logging
from memory_profiler import profile # for printing the memory usage if the function
import warnings
warnings.filterwarnings("ignore") #to ignore warnings throught the script

#defining log file
current_loc = os.getcwd()
try:
    os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Intelligent Weather Prediction Pipeline/src/data/logs")
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

if __name__ == "__main__":
    #check code is running currectly or not
    print("current location: ", current_loc)
    load_data("open-meteo-26.61N81.26E120m","C:/Users/KISHORE/OneDrive/Desktop/Intelligent Weather Prediction Pipeline/data/raw")




