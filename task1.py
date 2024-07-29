"""
Python script which, given an API URL specified in a .env file, will
request JSON data of books with a title containing 'lord of the rings'.
This data will be written into a JSON file to be kept as historical data,
A pandas DataFrame - with columns 'book_title', 'author_name', 'average_rating', 
'languages', 'locations_published' - will be the final output.
"""

from datetime import datetime
import json
from os import environ as ENV

import requests
from dotenv import load_dotenv
import pandas as pd


def get_lord_of_the_rings_books() -> list[dict]:
    """Returns all books with the title 'lord of the rings'."""

    response = requests.get(
        ENV["API_URL"] + ".json?title=the+lord+of+the+rings")

    if response.status_code == 200:

        result = response.json()

        return result

    print("Failed to retrieve data from the API. Status code:",
          response.status_code)


def input_api_data_into_json_file(json_data: dict, json_file: str) -> None:
    """Given a JSON dict object, it writes it into a JSON file of a given name."""

    if len(json_data) == 0:
        return None

    existing_data = []

    existing_data.append(json_data)

    with open(json_file, "w", encoding="utf-8") as g:
        json.dump(existing_data, g, indent=4)


def create_pd_df_titles(api_response: dict) -> pd.DataFrame:
    """
    Given our API response, we take all titles of books
    in the response, and input them into a pd.DataFrame object.
    """

    book_titles = [doc["title"] for doc in api_response["docs"]]

    authors = [doc["author_name"] for doc in api_response["docs"]]

    avg_ratings = [doc["ratings_average"] for doc in api_response["docs"]]

    languages = [doc["language"] for doc in api_response["docs"]]

    locations = [doc["publish_place"] for doc in api_response["docs"]]

    result_df = pd.DataFrame({"book_title": book_titles,
                              "author_name": authors,
                              "average_rating": avg_ratings,
                              "languages": languages,
                              "locations_published": locations})

    return result_df


def remove_duplicate_titles_no_case(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pd.DataFrame object with a column 'book_title', we
    remove duplicate values via a case-insensitive comparison.
    """
    pass


if __name__ == "__main__":

    load_dotenv()

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = today_date + "_lord_of_the_rings.json"

    result = get_lord_of_the_rings_books()

    if result is not None:
        input_api_data_into_json_file(result, json_filename)

    # TODO: Write extracted JSON data into a .json file
