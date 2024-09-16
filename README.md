# Howard Man's submission for the Datatonic Graduate Programme Technical Exercise

## Overview & Motivation
Hello, and welcome to my submission for the Datatonic Graduate Programme Technical Exercise. My name is Howard, and my submission involves extracting, wrangling, and analysing data for space-related books.

For Task 1, my final product was a `pandas` DataFrame object, with columns for book title, author name, number of languages the book was published in, average rating, and all dates the book was published. I cached the data extracted from the Open Library via a `JSON` file, to reduce compute resources.

For Task 2, I had a technically similar approach to Task 1, except I cached the `pandas` DataFrame into a `CSV` file. The column for all published dates was replaced with the year the book was first published.

For Task 3, I chose to visualise the data via `streamlit`, illustrating how many books were released per year, the top 10 books with most languages published, the top 10 authors with most books published, and the top 10 books with the highest average rating.

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

- `task1`: Contains code related to Task 1 of the Technical Exercise.
    - Uses the environment variable `API_BASE_URL = "https://openlibrary.org/search"`.
    - To run the code in this directory, input `python3 main.py` into the command-line interface.
    - An example of the extracted JSON data is in `task1/example_extracted.json`.

- `task2_task3`: Contains code related to Tasks 2 and 3 of the Technical Exercise.
    - To run the code in this directory, input `python3 -m streamlit run main.py` into the command-line interface.
    - An example of the extracted JSON data for Task 2 is not provided, due to size constraints. Though an example of the wrangled `pandas` DataFrame is available in CSV format at `task2_task3/example_space.csv`.
    - Contains another directory `example_diagrams`, containing examples of how the data visualisations should look on the Streamlit dashboard.
