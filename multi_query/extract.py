"""
Python script which, given an API base URL and a list of search queries - stated
as environment variables - will request JSON data of books, where each title of
the books satisfy at least one search query.

(Eg. if the list of search queries is ['green+apple', 'banana+cake', 'pear'],
every book in the response will have a title containing one or more of the 
phrases 'green apple', 'banana cake', 'pear').

Each response will be written into a JSON file, and this file will be named after
the date the response was extracted, as well as the search query.
"""

from datetime import datetime
import json
from os import environ as ENV, path

import requests
from dotenv import load_dotenv


API_BASE_URL = "https://openlibrary.org/search"
SEARCH_QUERIES_LIST=['space', 'space+flight', 'space+station',
                      'outer+space', 'space+exploration', 'space+and+time',
                      'space+vehicles', 'space+warfare', 'space+shuttles',
                      'space+stations', 'space+ships', 'moon', 'mars']


def get_all_queries_responses() -> list[dict]:
    """Returns all of the API responses for each of the search queries
    in SPACE_SEARCH_QUERIES."""

    result = []

    for query in SEARCH_QUERIES_LIST:

        response = requests.get(f"{API_BASE_URL}.json?q={query}",
            timeout=15)

        if response.status_code == 200:

            result.append(response.json())

        else:
            print("Failed to retrieve data from the API. Status code:",
            response.status_code)

    return result


def api_data_into_json(json_data: list[dict], json_file: str) -> None:
    """Given a JSON dict object, it writes it into a JSON file of a given name."""

    if len(json_data) != 0:

        with open(json_file, "w", encoding="utf-8") as g:
            json.dump(json_data, g, indent=4)


if __name__ == "__main__":

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_multi.json"

    multi_query_data = get_all_queries_responses()

    if multi_query_data is not None and not path.isfile(f"./{json_filename}"):
        api_data_into_json(multi_query_data, json_filename)
