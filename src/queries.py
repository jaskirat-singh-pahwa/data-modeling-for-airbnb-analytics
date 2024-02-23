"""
This module has few queries which could be the most important for the business.
Also, these queries will also have a nice visualization on the Streamlit UI. 
"""

import hashlib
from typing import Dict


QUERY_1 = """
SELECT hl.host_id, 
       COUNT(r.average_review_score) AS total_times_highest_score, 
       h.host_name
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
JOIN review r ON hl.review_id = r.review_id
WHERE r.average_review_score = 'A'
GROUP BY hl.host_id, 
         h.host_name 
ORDER BY total_times_highest_score DESC
LIMIT 10;
"""

QUERY_2 = """
SELECT host_response_time, 
       COUNT(*) AS number_of_hosts
FROM hosts
WHERE host_response_time IS NOT NULL
GROUP BY host_response_time
ORDER BY number_of_hosts DESC;
"""

QUERY_3 = """
SELECT h.host_name, 
       COUNT(*) AS num_listings
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
GROUP BY h.host_name
ORDER BY num_listings DESC
LIMIT 10;
"""

QUERY_4 = """
SELECT ROUND(AVG(listings_per_host) :: Numeric, 2) AS average_listings_per_host
FROM (
    SELECT host_id, 
           COUNT(*) AS listings_per_host
    FROM house_listings
    GROUP BY host_id
) AS subquery;
"""

QUERY_5 = """
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

QUERY_6 = """
SELECT zipcode, 
       COUNT(DISTINCT listing_id) AS total_properties
FROM house_listings
GROUP BY zipcode
ORDER BY total_properties DESC 
LIMIT 10;
"""

QUERY_7 = """
SELECT h.property_type, 
       ROUND(AVG(amenities_score) :: numeric, 2) average_amenities_score
FROM house_listings h
JOIN amenities a ON h.amenities_id = a.amenities_id
GROUP BY h.property_type
ORDER BY average_amenities_score DESC;
"""


def get_hash_id(query) -> str:
    """ 
        This function is to get hash value 
    """
    processed_query = " ".join(query.split())
    query_hash = hashlib.sha256(processed_query.encode()).hexdigest()

    return query_hash


def get_default_query_hashes() -> Dict[str, str]:
    """
        This function is to create a dictionary of all default queries as keys 
        and their hash ids as values 
    """
    queries_with_hash_id: Dict[str, str] = {
        "query_1": get_hash_id(query=QUERY_1),
        "query_2": get_hash_id(query=QUERY_2),
        "query_3": get_hash_id(query=QUERY_3),
        "query_4": get_hash_id(query=QUERY_4),
        "query_5": get_hash_id(query=QUERY_5),
        "query_6": get_hash_id(query=QUERY_6),
        "query_7": get_hash_id(query=QUERY_7)

    }

    return queries_with_hash_id
