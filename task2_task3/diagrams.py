"""Python script to produce diagrams for the final dashboard."""

from datetime import datetime

import pandas as pd
import altair as alt
from altair import datum

from wrangle import (load_json_data, create_pd_df, remove_duplicate_nan_values_format_cols_df)


def last_100_years(year: int):
    """Returns True if a given year is 100 years less than/equal to
    the current year, and False otherwise"""
    this_year = int(datetime.today().year)

    if this_year - year <= 100:
        return True

    return False


def create_yearly_count_books_100yrs(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Edits the pd.DataFrame object to only show books released within
    the last 100 years, adding in years that are missing in the input 
    pd.DataFrame object.
    """
    this_year = int(datetime.today().year)

    years_df = input_df["first_published"].value_counts().reset_index()

    years_df = years_df.rename(columns={'first_published': 'Year Published',
                                        'count': 'Number of Books Published'})

    years_df["last_100_years"] = years_df["Year Published"].apply(last_100_years)

    years_df = years_df[years_df["last_100_years"] == True].reset_index()

    years_df.drop(columns=['last_100_years', 'index'], inplace=True)

    n = len(years_df)

    existing_years = {years_df.loc[i]["Year Published"] for i in range(n)}

    valid_years = set(range(this_year - 100, this_year + 1))

    missing_years = list(valid_years - existing_years)

    for year in missing_years:

        m = len(years_df)

        years_df.loc[m] = [year, 0]

    return years_df


def create_books_released_per_year(input_df: pd.DataFrame) -> alt.Chart:
    """Returns a line chart showcasing the number of books released per year."""

    chart = alt.Chart(input_df, 
                title='Book Releases by Year').mark_line().encode(
        x=alt.X('Year Published:N'),
        y='Number of Books Published:Q'
    )

    return chart


def create_books_languages_bar_chart(input_df: pd.DataFrame) -> alt.Chart:
    """Creates a bar chart showcasing how many languages a given book has
    been published in."""

    language_df = input_df[['book_title', 'no_of_languages']]

    language_df.sort_values(by=['no_of_languages'], inplace=True, ascending=False)

    language_df = language_df.iloc[[str(i) for i in range(10)]]

    language_df = language_df.rename(columns={'book_title': 'Book Title',
                                'no_of_languages': 'Number of Languages'})

    chart = alt.Chart(language_df,
        title="Top 10 books published in the most languages"
        ).mark_bar().encode(
            x=alt.X('Number of Languages:Q'),
            y='Book Title:N'
        )

    return chart


def create_books_authors_pie_chart(input_df: pd.DataFrame) -> alt.Chart:
    """Creates a pie chart showcasing how many books each author has published."""

    author_df = input_df[['book_title', 'author_name']]

    author_data = author_df['author_name'].value_counts().reset_index()

    author_data = author_data.sort_values(by=['count'], ascending=False)

    author_data = author_data.iloc[[str(i) for i in range(10)]]

    author_data = author_data.rename(columns={'author_name': 'Author',
                                              'count': 'Number of Books'})

    chart = alt.Chart(author_data,
        title="Top 10 authors with the most books published"
        ).mark_arc().encode(
            color='Author',
            theta='Number of Books:Q'
        )

    return chart


def create_books_rating_bar_chart(input_df: pd.DataFrame) -> alt.Chart:
    """Creates a bar chart showcasing the average rating of each book."""

    rating_df = input_df[['book_title', 'average_rating']]

    rating_df.sort_values(by=['average_rating'], inplace=True, ascending=False)

    rating_df = rating_df.iloc[[str(i) for i in range(10)]]

    rating_df = rating_df.rename(columns={'book_title': 'Book Title',
                                          'average_rating': 'Average Rating'})

    chart = alt.Chart(rating_df, 
            title="Top 10 Books with the highest rating").mark_bar().encode(
        x=alt.X('Average Rating:Q'),
        y='Book Title'
    )

    return chart


if __name__ == "__main__":

    space_data = load_json_data("2024-08-11_space.json")

    space_df = create_pd_df(space_data)

    formatted_space_df = remove_duplicate_nan_values_format_cols_df(space_df)

    years_df = create_yearly_count_books_100yrs(formatted_space_df)

    create_books_released_per_year(years_df)