"""
    This module is to run queries on web UI using streamlit for Airbnb database.
"""
import hashlib
import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


db_params = {
    'host': 'localhost',
    'database': 'Airbnb_listings',
    'user': 'postgres',
    'password': 'Pass@12345',
}

query_1 = """
SELECT hl.host_id, COUNT(r.average_review_score) AS total_times_highest_score, h.host_name
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
JOIN review r on hl.review_id = r.review_id
WHERE r.average_review_score = 'A'
GROUP BY hl.host_id, h.host_name 
ORDER BY total_times_highest_score DESC
LIMIT 10;
"""

query_2 = """
SELECT host_response_time, COUNT(*) AS number_of_hosts
FROM hosts
WHERE host_response_time IS NOT NULL
GROUP BY host_response_time
ORDER BY number_of_hosts DESC;
"""

query_3 = """
SELECT h.host_name, COUNT(*) AS num_listings
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
GROUP BY h.host_name
ORDER BY num_listings DESC
LIMIT 10;
"""

query_4 = """
SELECT ROUND(AVG(listings_per_host) :: Numeric, 2) AS average_listings_per_host
FROM (
    SELECT host_id, COUNT(*) AS listings_per_host
    FROM house_listings
    GROUP BY host_id
) AS subquery;
"""

query_5 = """
SELECT
	CASE
		WHEN a.amenities_score BETWEEN 0 and 10 THEN '0-10'
		WHEN a.amenities_score BETWEEN 11 and 20 THEN '11-20'
		WHEN a.amenities_score BETWEEN 21 and 30 THEN '21-30'
		WHEN a.amenities_score BETWEEN 31 and 40 THEN '31-40'
		ELSE '41-55'
	END AS score_bucket,
	COUNT(DISTINCT h.host_id) AS num_hosts
FROM house_listings h
JOIN amenities a ON h.amenities_id = a.amenities_id
GROUP BY score_bucket
ORDER BY score_bucket;
"""

query_6 = """
SELECT zipcode, COUNT(DISTINCT listing_id) AS total_properties
FROM house_listings
GROUP BY zipcode
ORDER BY total_properties DESC 
LIMIT 10;
"""

query_7 = """
SELECT h.property_type, ROUND(AVG(amenities_score) :: numeric, 2) average_amenities_score
FROM house_listings h
JOIN amenities a ON h.amenities_id = a.amenities_id
GROUP BY h.property_type
ORDER BY average_amenities_score DESC;
"""


def hash_query(query):
    """ 
        This module is to get hash value 
    """
    processed_query = ' '.join(query.split())
    query_hash = hashlib.sha256(processed_query.encode()).hexdigest()
    return query_hash


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


def main():
    """
        This is the main entry point of the module.
    """
    st.title("Airbnb House Listings Query Runner")

    # Input for SQL Query
    query = st.text_area("Enter your SQL query:")

    # Button to execute the query
    # if st.button("Run Query"):
    #     if query:
    #         result_df = run_query(query)
    #         st.dataframe(result_df)
    #         plot_graph(user_input=query, result_df=result_df)
    #     else:
    #         st.warning("Please enter a query.")


if __name__ == "__main__":
    main()
