"""
    This module is to run queries on web UI using streamlit for Airbnb database.
"""
import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt



# db_params = {
#     'host': 'localhost',
#     'database': 'Airbnb_listings',
#     'user': 'postgres',
#     'password': 'Pass@12345',
# }


def plot_graph(user_input, result_df):
    """
        This function is to plot graphs
    """
    query_1_hash = hash_query(query=query_1)
    query_2_hash = hash_query(query=query_2)
    query_3_hash = hash_query(query=query_3)
    query_4_hash = hash_query(query=query_4)
    query_5_hash = hash_query(query=query_5)
    query_6_hash = hash_query(query=query_6)
    query_7_hash = hash_query(query=query_7)


    # Check if the query hash matches the user input hash
    user_input_hash = hash_query(query=user_input)

    if query_1_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['host_name'], result_df['total_times_highest_score'], color='thistle')
        ax.set_xlabel('Host Name')
        ax.set_ylabel('Total Number of "A" Scores')
        ax.set_title('Host Name vs Number of "A" Scores')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    elif query_2_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['host_response_time'], result_df['number_of_hosts'], color='skyblue')
        ax.set_xlabel('Host Response Time')
        ax.set_ylabel('Number of Hosts')
        ax.set_title('Host Response Time vs Number of Hosts')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    elif query_3_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['host_name'], result_df['num_listings'], color='orchid')
        ax.set_xlabel('Host Names')
        ax.set_ylabel('Number of Listings')
        ax.set_title('Number of Listings vs Host Names')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    elif query_4_hash == user_input_hash:
        st.markdown(
            f"**Average Listings per Host:** {result_df['average_listings_per_host'].iloc[0]:.2f}"
        )

    elif query_5_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['score_bucket'], result_df['num_hosts'], color='wheat')
        ax.set_xlabel('Score Bucket')
        ax.set_ylabel('Number of Hosts')
        ax.set_title('Amenities Score Bucket vs Number of Hosts')
        st.pyplot(fig)

    elif query_6_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['zipcode'], result_df['total_properties'], color='rosybrown')
        ax.set_xlabel('Zipcode')
        ax.set_ylabel('Number of Properties')
        ax.set_title('Zipcode vs Number of Properties')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    elif query_7_hash == user_input_hash:
        fig, ax = plt.subplots()
        ax.bar(result_df['property_type'], result_df['average_amenities_score'], color='burlywood')
        ax.set_xlabel('Property Type')
        ax.set_ylabel('Average Amenities Score')
        ax.set_title('Property Type vs Average Amenities Score')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    else:
        st.warning("Unsupported query. No data to plot.")


def run_query(query):
    """
        This function is used to run query from web UI and return the output as pandas dataframe.
    """
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    # Get column names from the cursor description
    columns = [desc[0] for desc in cursor.description]

    # Create a Pandas DataFrame
    df = pd.DataFrame(result, columns=columns)

    connection.close()
    return df


def main() -> None:
    """
        This is the main entry point of the module.
    """
    st.title("Airbnb House Listings Query Runner")

    # Input for SQL Query
    input_query: str = st.text_area("Enter your SQL query:")

    # Button to execute the query
    if st.button("Run Query"):

        if input_query:
            result: pd.DataFrame = run_query(input_query)
            st.dataframe(result)
            plot_graph(user_input=input_query, result_df=result)

        else:
            st.warning("Please enter a query.")


if __name__ == "__main__":
    main()
