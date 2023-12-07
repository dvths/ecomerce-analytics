import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from olist_data_extractor import OlistDataExtractor
from olist_data_loader import OlistDataLoader

load_dotenv()


def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # breakpoint()
    DATA_DIR = os.path.join(BASE_DIR, "data")
    DATA_RAW = os.path.join(DATA_DIR, "raw")
    ZIP_FILE = "olist_data.zip"

    CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
    DB = create_engine(CONNECTION_STRING)

    olist_extractor = OlistDataExtractor(
        zip_file=ZIP_FILE, data_dir=DATA_DIR, output_path=DATA_RAW
    )

    olist_extractor.extract_data()

    olist_loader = OlistDataLoader(datasets_path=DATA_RAW, database_engine=DB)

    olist_loader.load_data()


if __name__ == "__main__":
    main()
