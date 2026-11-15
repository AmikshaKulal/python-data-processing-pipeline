
import pandas as pd


def transform_data(df):

    # Convert ID if available
    if "id" in df.columns:
        df["id"] = pd.to_numeric(df["id"], errors="coerce")

    # Convert age if available
    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Convert salary if available
    if "salary" in df.columns:
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # Convert names to uppercase
    if "name" in df.columns:
        df["name"] = df["name"].apply(
            lambda x: x.upper() if isinstance(x, str) else x
        )

    # Calculate annual salary if salary exists
    if "salary" in df.columns:
        df["annual_salary"] = df["salary"] * 12

    return df
