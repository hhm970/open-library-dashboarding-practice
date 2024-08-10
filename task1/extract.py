"""
Python script which, given an API base URL specified in an .env file, will
request JSON data of books with a title containing 'lord of the rings'.
This data will be written into a JSON file, named after the date the response 
was extracted, as well as the search query title.
"""

from datetime import datetime
import json
from os import environ as ENV, path

import requests
from dotenv import load_dotenv


SEARCH_QUERY_TITLE = "the+lord+of+the+rings"


def get_lord_of_the_rings_books() -> list[dict]:
    """Returns all books with the title 'lord of the rings'."""

    response = requests.get(
        ENV["API_BASE_URL"] + f".json?title={SEARCH_QUERY_TITLE}",
        timeout=10)

    if response.status_code == 200:

        result = response.json()

        return result

    print("Failed to retrieve data from the API. Status code:",
          response.status_code)


def api_data_into_json(json_data: dict, json_file: str) -> None:
    """Given a JSON dict object, it writes it into a JSON file of a given name."""

    if len(json_data) != 0:

        existing_data = []

        existing_data.append(json_data)

        with open(json_file, "w", encoding="utf-8") as g:
            json.dump(existing_data, g, indent=4)

    return None


if __name__ == "__main__":

    load_dotenv()

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_{SEARCH_QUERY_TITLE}.json"

    extracted_data = get_lord_of_the_rings_books()

    if extracted_data is not None and not path.isfile(f"./{json_filename}"):
        api_data_into_json(extracted_data, json_filename)
