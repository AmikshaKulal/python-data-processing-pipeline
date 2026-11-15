import os


def write_data(df, output_path):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)

    elif output_path.endswith(".json"):
        df.to_json(output_path, orient="records", indent=4)

    else:
        raise ValueError("Unsupported output format")

    print(f"Output saved successfully: {output_path}")