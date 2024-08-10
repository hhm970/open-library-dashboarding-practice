"""
Python script which, given an API base URL specified in an .env file, will
request JSON data of books with the queries 'space', 'space flight', 'space station', 
'outer_space', 'space_exploration'.
This data will be written into a JSON file, named after the date the response 
was extracted, as well as the search query title.
"""

from datetime import datetime
import json
from os import environ as ENV, path

import requests
from dotenv import load_dotenv


SPACE_SEARCH_QUERIES={'space', 'space flight', 'space station', 
                      'outer_space', 'space_exploration'}
YEAR_OF_MOON_LANDING=1969

if __name__ == "__main__":
    load_dotenv()