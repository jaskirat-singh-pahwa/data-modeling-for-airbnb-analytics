"""
    This module is to plot graphss for all the default queries 
    that the user will input
"""

from typing import Dict

import matplotlib.pyplot as plt
import streamlit as st

from queries import (
    get_hash_id,
    get_default_query_hashes
)


def plot_graph(user_input, result_df) -> None:
    """
        This function is to plot graphs
    """
    default_queries_with_hashes: Dict[str, str] = get_default_query_hashes()

    # Check if the query hash matches the user input hash
    user_input_hash: str = get_hash_id(query=user_input)

    if user_input_hash == default_queries_with_hashes["query_1"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["host_name"], result_df["total_times_highest_score"], color="thistle")
        ax.set_xlabel("Host Name")
        ax.set_ylabel('Total Number of "A" Scores')
        ax.set_title('Host Name vs Number of "A" Scores')
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    elif user_input_hash == default_queries_with_hashes["query_2"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["host_response_time"], result_df["number_of_hosts"], color="skyblue")
        ax.set_xlabel("Host Response Time")
        ax.set_ylabel("Number of Hosts")
        ax.set_title("Host Response Time vs Number of Hosts")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    elif user_input_hash == default_queries_with_hashes["query_3"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["host_name"], result_df["num_listings"], color="orchid")
        ax.set_xlabel("Host Names")
        ax.set_ylabel("Number of Listings")
        ax.set_title("Number of Listings vs Host Names")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    elif user_input_hash == default_queries_with_hashes["query_4"]:
        st.markdown(
            f"**Average Listings per Host:** {result_df['average_listings_per_host'].iloc[0]:.2f}"
        )

    elif user_input_hash == default_queries_with_hashes["query_5"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["score_bucket"], result_df["num_hosts"], color="wheat")
        ax.set_xlabel("Score Bucket")
        ax.set_ylabel("Number of Hosts")
        ax.set_title("Amenities Score Bucket vs Number of Hosts")
        st.pyplot(fig)

    elif user_input_hash == default_queries_with_hashes["query_6"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["zipcode"], result_df["total_properties"], color="rosybrown")
        ax.set_xlabel("Zipcode")
        ax.set_ylabel("Number of Properties")
        ax.set_title("Zipcode vs Number of Properties")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    elif user_input_hash == default_queries_with_hashes["query_7"]:
        fig, ax = plt.subplots()
        ax.bar(result_df["property_type"], result_df["average_amenities_score"], color="burlywood")
        ax.set_xlabel("Property Type")
        ax.set_ylabel("Average Amenities Score")
        ax.set_title("Property Type vs Average Amenities Score")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    else:
        st.text("Visualization is not available, we are working on it!")
        st.dataframe(result_df)
