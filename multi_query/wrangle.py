"""
Using our extracted JSON file, we form a pandas DataFrame containing details
of each book, including the book title, author name, number of languages published,
average rating of the book, and the year the book was first published. 
The data is then cleaned for duplicates and empty values.
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

    unique_key = []

    book_titles = []

    authors = []

    avg_ratings = []

    language_count = []

    first_published = []

    for response_dict in api_response:

        for doc in response_dict["docs"]:

            unique_key.append(doc["key"])

            try:
                book_titles.append(f"{doc['title']}: {doc['subtitle']}")
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
                first_published.append(doc["first_publish_year"])
            except KeyError:
                first_published.append(None)

    result_df = pd.DataFrame({"unique_key": unique_key,
                              "book_title": book_titles,
                              "author_name": authors,
                              "average_rating": avg_ratings,
                              "no_of_languages": language_count,
                              "first_published": first_published})

    return result_df


def remove_duplicate_nan_values_format_cols_df(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pd.DataFrame object, returns the object such that all empty
    values are removed, and the 'no_of_languages' column stores integers.
    """
    result_df = input_df.dropna().drop_duplicates(subset=['unique_key']).reset_index()

    result_df["first_published"] = result_df["first_published"].astype("int64")

    result_df["no_of_languages"] = result_df["no_of_languages"].astype("int64")

    result_df.drop(['unique_key', 'index'], axis=1, inplace=True)

    return result_df


if __name__ == "__main__":

    space_data = load_json_data("2024-09-16_multi.json")

    space_df = create_pd_df(space_data)

    formatted_space_df = remove_duplicate_nan_values_format_cols_df(space_df)

    print(formatted_space_df)
