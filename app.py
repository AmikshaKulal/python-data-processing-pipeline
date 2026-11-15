
import streamlit as st
import pandas as pd
import json
from src.cleaner import clean_data
from src.transformer import transform_data

st.set_page_config(
    page_title="Python Data Processing Pipeline",
    page_icon="📊"
)

st.title("📊 Python Data Processing Pipeline")
st.write("Upload CSV or JSON data, clean it, transform it, and download the results.")

uploaded_file = st.file_uploader(
    "Upload your CSV or JSON file",
    type=["csv", "json"]
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            data = json.load(uploaded_file)
            if isinstance(data, dict):
                data = data.get("data", [data])
            if not isinstance(data, list):
                st.error("JSON must contain a list of records.")
                st.stop()
            df = pd.DataFrame(data)

        st.subheader("Original Data")
        st.dataframe(df)

        if st.button("Process Data"):
            cleaned_df = clean_data(df)
            result_df = transform_data(cleaned_df)

            st.subheader("Processed Data")
            st.dataframe(result_df)

            csv_data = result_df.to_csv(index=False).encode("utf-8")
            json_data = result_df.to_json(
                orient="records", indent=4
            ).encode("utf-8")

            st.download_button(
                "Download CSV",
                csv_data,
                "cleaned_data.csv",
                "text/csv"
            )

            st.download_button(
                "Download JSON",
                json_data,
                "cleaned_data.json",
                "application/json"
            )

            st.success("Data processed successfully!")

    except Exception as e:
        st.error(f"Processing failed: {e}")
