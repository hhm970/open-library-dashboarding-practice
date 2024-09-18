"""Python script to produce diagrams for the final dashboard."""

from datetime import datetime

import pandas as pd
import altair as alt

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

    base = alt.Chart(input_df, title='Book Releases by Year')

    chart = base.mark_line().encode(
        x='Year Published:Q',
        y='Number of Books Published:Q'
    ).interactive()

    xrule = base.mark_rule(color="red", strokeDash=[2, 2]).encode(
        x=alt.datum(1969)
    )

    return chart + xrule


def create_rating_languages_scatter(input_df: pd.DataFrame) -> alt.Chart:
    """Returns a scatter graph with number of languages on the x-axis,
    and average rating on the y-axis."""

    scatter_df = input_df[["book_title", "author_name",
                           "average_rating", "no_of_languages"]]

    scatter_df = scatter_df.rename(columns={"average_rating": "Average Rating",
                               "no_of_languages": "Number of Languages Published",
                               "book_title": "Book Title",
                               "author_name": "Author"
                               })

    chart = alt.Chart(scatter_df,
                      title="Book Rating over Number of Languages Published"
                ).mark_circle(size=200).encode(
            x='Number of Languages Published:Q',
            y='Average Rating:Q',
            tooltip=["Book Title",
                     "Author",
                     "Average Rating",
                     "Number of Languages Published"]
        ).interactive()

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
        ).interactive()

    return chart


def create_books_authors_pie_chart(input_df: pd.DataFrame) -> alt.Chart:
    """Creates a pie chart showcasing how many books each author has published."""

    author_df = input_df[['book_title', 'author_name']]

    author_data = author_df['author_name'].value_counts().reset_index()

    author_data = author_data.sort_values(by=['count'], ascending=False)

    author_data = author_data.iloc[[str(i) for i in range(10)]]

    author_data = author_data.rename(columns={'author_name': 'Author',
                                              'count': 'Number of Books'})

    base = alt.Chart(author_data,
        title="Top 10 authors with the most books published"
        ).encode(alt.Theta('Number of Books:Q').stack(True),
            color='Author:N'
        )
    
    pie = base.mark_arc(outerRadius=200)
    text = base.mark_text(radius=240, size=20).encode(text='Number of Books:Q')

    return pie + text


def create_books_rating_bar_chart(input_df: pd.DataFrame) -> alt.Chart:
    """Creates a bar chart showcasing the average rating of each book."""

    total_average_rating = input_df['average_rating'].sum()

    total_no_of_ratings = len(input_df)

    agg_average_rating = total_average_rating/total_no_of_ratings

    count_df = input_df['average_rating'].value_counts().reset_index()

    count_df.sort_values(by=['average_rating'], inplace=True, ascending=False)

    rating_df = count_df.rename(columns={'count': 'Number of Books',
                                          'average_rating': 'Average Rating'})

    base = alt.Chart(rating_df,
            title="Distribution of Ratings Across Books"
            ).encode(
                x='Average Rating:Q',
                y='Number of Books:Q'
            )

    chart = base.mark_line().interactive()

    xrule = base.mark_rule(color="red", strokeDash=[2, 2]).encode(
        x=alt.datum(agg_average_rating)
    )

    return chart + xrule


if __name__ == "__main__":

    space_data = load_json_data("2024-09-16_multi.json")

    space_df = create_pd_df(space_data)

    formatted_space_df = remove_duplicate_nan_values_format_cols_df(space_df)

    years_df = create_yearly_count_books_100yrs(formatted_space_df)

    create_books_released_per_year(years_df)
