from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parents[2]

with open(ROOT_DIR / "config.yaml", "r") as file:
    config = yaml.safe_load(file)

name = config["project"]["name"]
print(name)

RAW_DATA = config["paths"]["raw_data"]
REPORTS = config["paths"]["Reports"]
INTERIM = config["paths"]["Interim"]
CLEAN_DATA_FILE = config["files"]["Clean_data"]
CLN_DATA_FILE = config["files"]["Cln_data"]
PROCESSED = config["paths"]["Processed"]
PROCESSED_DATA = config["files"]["Processed_data"]
ARTIFACTS = config["paths"]["Artifacts"]
TRIAL_LOGS = config["paths"]["Trial_log"]
FIGURES = config["paths"]["Figures"]
MODELS = config["paths"]["Models"]


