"""
Python script which, given an API base URL specified in an .env file, will
request JSON data of books for each of the search queries 'space', 'space flight', 
'space station', 'outer_space', 'space_exploration'.
Each response will be written into a JSON file, named after the date the response 
was extracted, as well as the search query.
"""

from datetime import datetime
import json
from os import environ as ENV, path

import requests
from dotenv import load_dotenv


SPACE_SEARCH_QUERIES=['space', 'space+flight', 'space+station', 
                      'outer+space', 'space+exploration']
YEAR_OF_MOON_LANDING=1969


def get_all_queries_responses() -> list[dict]:
    """Returns all of the API responses for each of the search queries
    in SPACE_SEARCH_QUERIES."""

    result = []

    for query in SPACE_SEARCH_QUERIES:

        response = requests.get(f"{ENV['API_BASE_URL']}.json?q={query}",
            timeout=15)

        if response.status_code == 200:

            result.append(response.json())

        else:
            print("Failed to retrieve data from the API. Status code:",
            response.status_code)

    return result


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

    json_filename = f"{today_date}_space.json"

    space_data = get_all_queries_responses()

    if space_data is not None and not path.isfile(f"./{json_filename}"):
        api_data_into_json(space_data, json_filename)