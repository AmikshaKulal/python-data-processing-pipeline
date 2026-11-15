import requests
import pandas as pd


def read_api(url):

    response = requests.get(url, timeout=15)

    response.raise_for_status()

    data = response.json()

    if isinstance(data, dict):
        data = data.get("data", [data])

    if not isinstance(data, list):
        raise ValueError("API must return a JSON list or object")

    return pd.DataFrame(data)