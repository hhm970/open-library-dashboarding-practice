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
                      create_rating_languages_scatter,
                      create_books_languages_bar_chart,
                      create_books_authors_pie_chart,
                      create_books_rating_line_chart)

API_BASE_URL = "https://openlibrary.org/search"
SPACE_SEARCH_QUERIES=['space', 'space+flight', 'space+station',
                      'outer+space', 'space+exploration', 'space+and+time',
                      'space+vehicles', 'space+warfare', 'space+shuttles',
                      'space+stations', 'space+ships', 'moon', 'mars']


def setup_metrics(input_df: pd.DataFrame) -> None:
    """Sets up metrics content on dashboard."""
    left, middle, right = st.columns(3)

    total_books = len(input_df)
    total_rating = input_df['average_rating'].sum()
    total_languages = input_df['no_of_languages'].sum()

    with left:
        st.metric("Total Number of Books", total_books)

    with middle:
        st.metric("Aggregated Average Rating for all Books", 
                  round(total_rating/total_books, 2))
        
    with right:
        st.metric("Aggregated Average Number of Languages Published",
                  round(total_languages/total_books, 2))


def setup_yearly_books_line_chart(input_df: pd.DataFrame) -> None:
    """Sets up chart for yearly release book count."""
    yearly_df = create_yearly_count_books_100yrs(input_df)
    yearly_books_line_chart = create_books_released_per_year(yearly_df)

    st.altair_chart(yearly_books_line_chart, use_container_width=True)


def setup_ratings_languages_scatter_chart(input_df: pd.DataFrame) -> None:
    """Sets up chart for comparing book rating over the number 
    of languages published."""

    scatter_chart = create_rating_languages_scatter(input_df)

    st.altair_chart(scatter_chart, use_container_width=True)


def setup_author_pie_chart(input_df: pd.DataFrame) -> None:
    """Sets up chart for the number of books released by each author."""

    author_pie_chart = create_books_authors_pie_chart(input_df)

    st.altair_chart(author_pie_chart, use_container_width=True)


def setup_2_bar_charts(input_df: pd.DataFrame) -> None:
    """Sets up chart for counting books by number of languages published,
    and a chart for the average rating per book."""

    language_bar_chart = create_books_languages_bar_chart(input_df)
    rating_bar_chart = create_books_rating_line_chart(input_df)

    left, right = st.columns(2)

    with left:
        st.altair_chart(language_bar_chart, use_container_width=True)

    with right:
        st.altair_chart(rating_bar_chart,
                        use_container_width=True)


def extract_wrangle_pd_df() -> pd.DataFrame:
    """Contains relevant steps for extraction and wrangling of data."""

    today_date = datetime.today().strftime('%Y-%m-%d')

    json_filename = f"{today_date}_multi.json"

    csv_filename = f"{today_date}_multi.csv"

    if not path.isfile(f"./{json_filename}"):

        multi_query_data = get_all_queries_responses()

        if multi_query_data is not None:

            api_data_into_json(multi_query_data, json_filename)

    else:

        multi_query_data = load_json_data(json_filename)

    if not path.isfile(f"./{csv_filename}"):

        multi_query_df = create_pd_df(multi_query_data)

        formatted_multi_df = remove_duplicate_nan_values_format_cols_df(
            multi_query_df)

        formatted_multi_df.to_csv(f"./{csv_filename}", index=False)

    else:

        formatted_multi_df = pd.read_csv(f"./{csv_filename}")

    return formatted_multi_df


if __name__ == "__main__":

    load_dotenv()

    st.set_page_config(page_title='Space Books Dashboard',
                       page_icon=":rocket:", layout="wide")

    space_df = extract_wrangle_pd_df()
    space_df_book_titles = space_df["book_title"].to_list()

    st.title("Welcome!")
    st.write("---")
    st.subheader("Containing all data from your favourite space-themed books!")

    setup_metrics(space_df)

    with st.sidebar:
        st.title("Space-related Books Dashboard")
        st.subheader("Collating information on all texts related to space!")
        st.write("---")

        st.title("Book Filter")

        creator_options = space_df_book_titles
        filtered_input = st.multiselect("Available Books",
                                       options=creator_options,
                                       default=creator_options)

    filtered_space_df = space_df[space_df["book_title"].isin(filtered_input)]

    setup_yearly_books_line_chart(filtered_space_df)

    setup_ratings_languages_scatter_chart(filtered_space_df)

    setup_2_bar_charts(filtered_space_df)

    setup_author_pie_chart(filtered_space_df)
