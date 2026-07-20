from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parents[2]

with open(ROOT_DIR / "config.yaml", "r") as file:
    config = yaml.safe_load(file)

RAW_DATA = config["paths"]["raw_data"]