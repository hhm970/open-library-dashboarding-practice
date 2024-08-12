"""
Using our extracted JSON file, we form a pandas DataFrame containing details
of each book, including the book title, author name, number of languages published,
average rating of the book, and all dates the book was published. The data is then
cleaned for duplicates and empty values.
"""

import json

import pandas as pd


def load_json_data(json_filename: str) -> list[dict]:
    """
    Given our JSON filename, we load the data, returning it as 
    a list[dict] object.
    """
    with open(json_filename, 'r', encoding='utf-8') as f:
        result = json.load(f)

    return result


def create_pd_df(api_response: dict) -> pd.DataFrame:
    """
    Given our JSON data, we take all titles of books
    in the response, and input them into a pd.DataFrame object.
    """

    book_titles = []

    authors = []

    avg_ratings = []

    language_count = []

    publish_dates = []

    for doc in api_response["docs"]:

        try:
            book_titles.append(doc["title"])
        except KeyError:
            book_titles.append(doc["title_suggest"])

        try:
            authors.append(doc["author_name"][0])
        except KeyError:
            try:
                authors.append(doc["author_alternative_name"][0])
            except KeyError:
                authors.append(None)

        try:
            avg_ratings.append(doc["ratings_average"])
        except KeyError:
            avg_ratings.append(None)

        try:
            language_count.append(len(doc["language"]))
        except KeyError:
            language_count.append(None)

        try:
            publish_dates.append(doc["publish_date"])
        except KeyError:
            publish_dates.append(None)

    result_df = pd.DataFrame({"book_title": book_titles,
                              "author_name": authors,
                              "average_rating": avg_ratings,
                              "no_of_languages": language_count,
                              "publish_dates": publish_dates})

    return result_df


def remove_nan_values_format_cols_df(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pd.DataFrame object, returns the object such that all empty
    values are removed, and the 'no_of_languages' column stores integers.
    """
    result_df = input_df.dropna().reset_index()

    result_df["no_of_languages"] = result_df["no_of_languages"].astype("int64")

    return result_df


if __name__ == "__main__":

    lotr_data = load_json_data("2024-08-05_the+lord+of+the+rings.json")[0]

    lotr_df = create_pd_df(lotr_data)

    lotr_df_no_nan = remove_nan_values_format_cols_df(lotr_df)

    print(lotr_df_no_nan)
