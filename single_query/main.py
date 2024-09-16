"""Main Python script to be run for Task 1."""
from datetime import datetime

from dotenv import load_dotenv
from os import environ as ENV, path

from extract import api_data_into_json, get_search_query_title_books
from wrangle import create_pd_df, remove_nan_values_format_cols_df

API_BASE_URL = "https://openlibrary.org/search"


if __name__ == "__main__":
    
    load_dotenv()

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_title={ENV['SEARCH_QUERY_TITLE']}.json"

    extracted_data = get_search_query_title_books()

    if extracted_data is not None and not path.isfile(f"./{json_filename}"):
        lotr_data = api_data_into_json(extracted_data, json_filename)[0]

    lotr_df = create_pd_df(lotr_data)

    lotr_df_no_nan = remove_nan_values_format_cols_df(lotr_df)

    print(lotr_df_no_nan)
