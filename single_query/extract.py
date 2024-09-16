"""
Python script which, given an API base URL, will request JSON data of books,
such that the title of the books correspond to a given search query, which is
stated as an environment variable.

(Eg. the search query for all titles containing the phrase 'the lord of the rings'
would be 'the+lord+of+the+rings').

This data will be written into a JSON file, named after the date the response 
was extracted, as well as the search query.
"""

from datetime import datetime
import json
from os import environ as ENV, path

import requests
from dotenv import load_dotenv


API_BASE_URL = "https://openlibrary.org/search"


def get_search_query_title_books() -> list[dict]:
    """Returns all books satisfying a given title search query."""

    response = requests.get(
        f"{API_BASE_URL}.json?title={ENV['SEARCH_QUERY_TITLE']}",
        timeout=10)

    if response.status_code == 200:

        result = response.json()

        return result

    print("Failed to retrieve data from the API. Status code: ",
          response.status_code)


def api_data_into_json(json_data: dict, json_file: str) -> None:
    """Given a JSON dict object, it writes it into a JSON file of a given name."""

    if len(json_data) != 0:

        existing_data = []

        existing_data.append(json_data)

        with open(json_file, "w", encoding="utf-8") as g:
            json.dump(existing_data, g, indent=4)

        return existing_data

    return None


if __name__ == "__main__":

    load_dotenv()

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_title={ENV['SEARCH_QUERY_TITLE']}.json"

    extracted_data = get_search_query_title_books()

    if extracted_data is not None and not path.isfile(f"./{json_filename}"):
        api_data_into_json(extracted_data, json_filename)
