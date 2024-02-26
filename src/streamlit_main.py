"""
    This module is to run queries on web UI using streamlit for Airbnb database.
"""
from typing import Dict, Optional, Tuple
import streamlit as st
import psycopg2
import pandas as pd

from plot_common_graphs import plot_graph


db_params: Dict[str, str] = {
    "host": "",
    "database": "",
    "user": "",
    "password": "",
}

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


def take_input_from_user() -> Optional[Tuple[Dict[str, str], str]]:
    try:
        while True:
            # Input DB credentials
            host = st.text_input("Enter the host name: ")
            database = st.text_input("Enter the database name: ")
            username = st.text_input("Enter your username: ")
            password = st.text_input("Enter your password: ", type="password")

            # Input for SQL Query
            user_input_query: str = st.text_area("Enter your SQL query:")

            if host and database and username and password:
                db_params["host"] = host
                db_params["database"] = database
                db_params["username"] = username
                db_params["password"] = password

                return db_params, user_input_query

            else:
                pass
                # Ask do you want to continue?

    except Exception as e:
        st.text(f"Exception occured: {e}")


def main() -> None:
    """
        This is the main entry point of the module.
    """
    st.title("Airbnb House Listings Query Runner")

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
