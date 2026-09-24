"""CLASS4 WE ARE WORKING ON DIFFEREWNT FILE TYPES"""

import json
import logging
from pathlib import Path
import os
import pandas as pd
import yaml
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # TODO:
    logger.info(f"Inspecting {filepath.suffix}:{filepath.name}")
    data = pd.read_csv(filepath)
    print(data.head(3))

def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TODO:
    logger.info(f"Inspecting {filepath.suffix}:{filepath.name}")
    with open(filepath, "r") as f:
        data = json.load(f)
    print(data)



def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # TODO:
    logger.info(f"Inspecting {filepath.suffix}:{filepath.name}")
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    print(data)
   



def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    logger.info(f"Inspecting ENV")
    print(keys)
    # TODO:


def main():
    # TODO:
    # 1. Create a Path object for the data directory.
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    data_dir = Path("data")
    csv_path = data_dir / "sample.csv"
    json_path = data_dir / "sample.json"
    yaml_path = data_dir / "sample.yaml"

    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)
    inspect_env()


if __name__ == "__main__":
    main()