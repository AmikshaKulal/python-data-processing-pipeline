import pandas as pd
import json
import os


def read_csv(file_path):
    return pd.read_csv(file_path)


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    return pd.DataFrame(data)


def read_data(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith(".csv"):
        return read_csv(file_path)

    elif file_path.endswith(".json"):
        return read_json(file_path)

    else:
        raise ValueError("Unsupported file format")