# Open Library Dashboarding Project

## Overview & Motivation
Hello, and welcome to my dashboarding data-science project for the Open Library! My name is Howard, and my project involves extracting, wrangling, and analysing data for space-related books. I conducted this project to get better at using Streamlit to create effective and clear data visualisations. 

I also chose to analyse space-related books, as I really wanted to see if the 1969 Moon Landings resulted in an increase in space-related book publications!

My project utilises two aspects of typical data-science projects:

- Extracting and wrangling data via the Open Library API (accessible via `https://openlibrary.org/search`);
- Presenting it clearly via data visualisations.

I firstly wanted to get a feel for extracting and wrangling data via responses from the Open Library API, hence I started with 1 search query in the `single_query` directory. My final product was a `pandas` DataFrame object, with columns for book title, author name, number of languages the book was published in, average rating, and all dates the book was published. I cached the data extracted from the Open Library via a `JSON` file, to reduce compute resources.

Afterwards, I wished to work with more data to create meaningful data visualisations, so I leveraged data via multiple search queries. My extraction and wrangling approach was similar to that of a singular query, except I cached the `pandas` DataFrame into a `CSV` file. The column for all published dates was replaced with the year the book was first published.

I then chose to visualise the data via `streamlit`, illustrating how many books were released per year, the top 10 books with most languages published, the top 10 authors with most books published, the distribution of average ratings across books, and a bivariate scatter graph measuring correlation between the average rating of a book and the number of languages it has been published in.

## Requirements

### Pre-requisites

- ```Python 3.11```
- `pip3`

### Imports
Each sub-folder in this repository holds their own `requirements.txt` file. This is has been done to ensure clarity in what modules the scripts require.

In each folder's directory to download the requirements use this command:

```sh
pip3 install -r requirements.txt
  ```

It is advised to run this command in a virtual environment (where each individual directory has its own virtual environment).

## Overview of Directories

This repository contains the following directories:

- `single_query`: Contains code related to extracting and wrangling data, given a singular search query.
    - Uses the environment variable `SEARCH_QUERY_TITLE`; more details on this are provided in the doc-string of `single_query/extract.py`.
    - To run the code in this directory, input `python3 main.py` into the command-line interface.
    - An example of some extracted JSON data is in `single_query/example_extracted.json`.

- `multi_query`: Contains code related to extracting and wrangling data, given multiple search queries, and displaying it via a Streamlit dashboard.
    - To run the code in this directory, input `python3 -m streamlit run main.py` into the command-line interface.
    - An example of possible extracted JSON data is not provided, due to size constraints. Though an example of the wrangled `pandas` DataFrame is available in CSV format at `multi_query/example_space.csv`.
    - Contains another directory `example_diagrams`, containing examples of possible data visualisations for the Streamlit dashboard.
