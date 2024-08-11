# Datatonic Graduate Programme Technical Exercise

## The Challenge

We would like you to showcase your Python (or other coding language e.g. Java, Golang etc.) skills by tackling a data wrangling challenge that involves the open library public data API.

### Tasks: 
1. Parse Available Datasets: 
+ Write a Python script that retrieves a list of all books with the title “lord of the rings” from the API https://openlibrary.org/dev/docs/api/search 
+ Parse the response from the API and write the names of the books to a dataset. Add 4 other columns showing data from the response 
2. Retrieve a Specific Dataset: 
+ Using any of the other API’s available in the above link, construct a dataset using a query that you have put together and fetched data for via the API. Use the examples listed as guidance on how to construct these queries 
3. Brief Dataset Exploration: 
+ Explore the data you collected in step 2 and produce some interesting insights in the data found including any charts/graphs/tables 

### Deliverables: 
+ A well-commented script / notebook demonstrating the tasks mentioned above. 

### Bonus Points: 
+ Implement error handling in your script to gracefully handle any issues encountered by either the API or subsequently collected data 

### Evaluation Criteria: 
+ Functionality (completing all tasks) 
+ Code clarity and structure 
+ Efficiency and error handling 
+ Creativity and approach to high-level dataset exploration

This challenge will assess your ability to interact with APIs, parse data, and perform basic data exploration using your language of choice.


# Howard Man's submission for the Datatonic Graduate Programme Technical Exercise

## Overview

## Requirements

### Pre-requisites

- ```Python 3.11```
- `pip3`
- `Terraform`

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

- `task2_task3`: Contains code related to Tasks 2 and 3 of the Technical Exercise.
    - Uses the environment variable `API_BASE_URL = "https://openlibrary.org/search"`.
    - To run the code in this directory, input `python3 -m streamlit run main.py` into the command-line interface


