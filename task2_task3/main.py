"""
Python script to be run to produce Streamlit dashboard showcasing
data insights.
"""

from datetime import datetime
from os import path

import pandas as pd
from dotenv import load_dotenv
import streamlit as st

from extract import get_all_queries_responses, api_data_into_json
from wrangle import (load_json_data, create_pd_df,remove_duplicate_nan_values_format_cols_df)
from diagrams import (create_books_released_per_year,
                      create_yearly_count_books_100yrs,
                      create_books_languages_bar_chart,
                      create_books_authors_pie_chart,
                      create_books_rating_bar_chart)

SPACE_SEARCH_QUERIES=['space', 'space+flight', 'space+station',
                      'outer+space', 'space+exploration', 'space+and+time',
                      'space+vehicles', 'space+warfare', 'space+shuttles',
                      'space+stations', 'space+ships', 'moon', 'mars']


def setup_sidebar() -> None:
    """Sets up sidebar content on dashboard."""
    st.sidebar.title("Space-related Books Dashboard")
    st.sidebar.subheader("Collating information on all texts related to space!")


def setup_metrics(df: pd.DataFrame) -> None:
    """Sets up metrics content on dashboard."""
    st.metric("Total Number of Books", len(df))


def setup_yearly_books_line_chart(input_df: pd.DataFrame) -> None:
    """Sets up chart for yearly release book count."""
    yearly_df = create_yearly_count_books_100yrs(input_df)
    yearly_books_line_chart = create_books_released_per_year(yearly_df)

    st.altair_chart(yearly_books_line_chart, use_container_width=True)


def setup_3_charts(input_df: pd.DataFrame) -> None:
    """Sets up chart for counting books by number of languages published,
    a chart to see the number of books released by each author, and a chart
    for the average rating per book."""

    language_bar_chart = create_books_languages_bar_chart(input_df)
    author_pie_chart = create_books_authors_pie_chart(input_df)
    rating_bar_chart = create_books_rating_bar_chart(input_df)

    left, middle, right = st.columns(3)

    with left:
        st.altair_chart(language_bar_chart, use_container_width=True)
    with middle:
        st.altair_chart(author_pie_chart,
                        use_container_width=True)
    with right:
        st.altair_chart(rating_bar_chart,
                        use_container_width=True)
        

def extract_wrangle_pd_df() -> pd.DataFrame:
    """Contains relevant steps for extraction and wrangling of data."""

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_space.json"

    csv_filename = f"{today_date}_space.csv"

    if not path.isfile(f"./{json_filename}"):

        space_data = get_all_queries_responses()

        if space_data is not None:

            api_data_into_json(space_data, json_filename)

    else:

        space_data = load_json_data(json_filename)

    if not path.isfile(f"./{csv_filename}"):

        space_df = create_pd_df(space_data)

        formatted_space_df = remove_duplicate_nan_values_format_cols_df(space_df)

        formatted_space_df.to_csv(f"./{csv_filename}", index=False)

    else:

        formatted_space_df = pd.read_csv(f"./{csv_filename}")

    return formatted_space_df


if __name__ == "__main__":

    load_dotenv()

    space_df = extract_wrangle_pd_df()

    st.title("Welcome!")
    st.write("---")
    st.subheader("Containing all data from your favourite space-themed books!")

    setup_metrics(space_df)

    setup_yearly_books_line_chart(space_df)

    setup_3_charts(space_df)
