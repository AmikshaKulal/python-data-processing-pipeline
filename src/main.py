
import yaml

from reader import read_data
from cleaner import clean_data
from transformer import transform_data
from writer import write_data
from logger import setup_logger
from api_reader import read_api


# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)


# Setup logger
logger = setup_logger(config["log_file"])


def main():

    try:
        logger.info("Pipeline started")

        # Read data from API or file
        if config["input_type"] == "api":
            df = read_api(config["api_url"])
            logger.info("API data loaded successfully")
        else:
            df = read_data(config["input_file"])
            logger.info("File data loaded successfully")

        # Clean data
        df = clean_data(df)
        logger.info("Data cleaning completed")

        # Transform data
        df = transform_data(df)
        logger.info("Data transformation completed")

        # Save output
        write_data(df, config["output_file"])
        logger.info("Output saved successfully")

        print("Pipeline executed successfully!")

    except Exception:
        logger.exception("Pipeline failed")
        print("Pipeline failed. Check logs for details.")


if __name__ == "__main__":
    main()
