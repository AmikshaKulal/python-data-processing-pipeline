
import pandas as pd


def clean_data(df):

    # Remove duplicate records safely
    df = df.drop_duplicates(
        subset=[
            col for col in df.columns
            if not df[col].apply(lambda x: isinstance(x, (dict, list))).any()
        ]
    )

    # Clean text columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        )

    # Replace empty strings with missing values
    df = df.replace(r"^\s*$", None, regex=True)

    # Handle missing values in numeric columns
    for col in df.columns:

        if col in ["age", "salary"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

            if df[col].notna().any():
                df[col] = df[col].fillna(df[col].median())

        else:
            df[col] = df[col].apply(
                lambda x: "Unknown" if x is None else x
            )

    return df
