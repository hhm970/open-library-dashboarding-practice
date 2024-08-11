"""
Python script to be run to produce Streamlit dashboard showcasing
data insights.
"""

import streamlit

from extract import get_all_queries_responses, api_data_into_json
from wrangle import (load_json_data, create_pd_df,
                     remove_duplic_nan_values_format_cols_df)


if __name__ == "__main__":
    pass