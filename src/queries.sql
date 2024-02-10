--------------------------------------- INSERT QUERIES ---------------------------------------------------
INSERT INTO house_listings (
	listing_id,
    listing_name,
    description,
    neighborhood_overview,
    zipcode,
    latitude,
    longitude,
    property_type,
    amenities_id,
    room_type,
    accommodates,
    bathrooms,
    beds,
    price,
    minimum_nights,
    maximum_nights,
    has_availability,
    availability_30,
    availability_60,
    availability_90,
    availability_365,
    review_id,
    host_id
)
VALUES (
	28081996,
    'Jaskirat - bramble cottage',
    'The place is beautiful, quiet and private',
    'Its in the hills, quiet neighbourhood',
    98109,
    '35.6521 ',
    '-78.3845',
    'Cottage',
    1022,
    'Entire Cottage',
    '14',
    10,
    16,
    '$1500.00',
    '2',
    '30',
    'Yes',
    '15',
    '30',
    '45',
    '150',
    3,
    110917
);

SELECT * FROM house_listings WHERE listing_id = 28081996;

----------------------------------------------------------
INSERT INTO neighbourhood (
	neighbourhood_id,
	neighbourhood,
	neighbourhood_cleansed
)
VALUES(
	82,
	'Delhi',
	'Tagore Garden'
);

SELECT * FROM neighbourhood WHERE neighbourhood_id = 82;



--------------------------------------- UPDATE QUERIES ---------------------------------------------------
UPDATE house_listings
SET
    listing_name = 'Jaskirat Singh Pahwa - bramble cottage'
WHERE
    listing_id = 28081996;

SELECT * FROM house_listings WHERE listing_id = 28081996;


-------------------------------------------
UPDATE neighbourhood
SET 
	neighbourhood_cleansed = 'Tagore Garden, 110027'
WHERE
	neighbourhood_id=82;
	
SELECT * FROM neighbourhood WHERE neighbourhood_id = 82;



--------------------------------------- DELETE QUERIES ---------------------------------------------------
DELETE FROM house_listings
WHERE listing_id = 953595;

SELECT * FROM house_listings WHERE listing_id = 953595;


------------------------------------------------------
DELETE FROM house_listings
WHERE listing_id = 3308979;

SELECT * FROM house_listings WHERE listing_id = 3308979;



--------------------------------------- SELECT QUERIES ----------------------------------------------------
SELECT * FROM amenities;
SELECT * FROM hosts;
SELECT * FROM locations;
SELECT * FROM neighbourhood;
SELECT * FROM review;
SELECT * FROM house_listings;


-- What is the total number of hosts for a given response time ? 
SELECT host_response_time, COUNT(*) AS number_of_hosts
FROM hosts
WHERE host_response_time IS NOT NULL
GROUP BY host_response_time
ORDER BY number_of_hosts DESC;


-- Top 10 hosts with highest Listings (Properties)
SELECT h.host_name, COUNT(*) AS num_listings
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
GROUP BY h.host_name
ORDER BY num_listings DESC
LIMIT 10;


-- Average number of listings per host
SELECT ROUND(AVG(listings_per_host) :: Numeric, 2) AS average_listings_per_host
FROM (
    SELECT host_id, COUNT(*) AS listings_per_host
    FROM house_listings
    GROUP BY host_id
) AS subquery;


-- Total Number of hosts within range of amenities scores
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


-- Top 10 zip_codes with highest number of properties
SELECT zipcode, COUNT(DISTINCT listing_id) AS total_properties
FROM house_listings
GROUP BY zipcode
ORDER BY total_properties DESC 
LIMIT 10;


-- Average amenities score for each property type
SELECT h.property_type, ROUND(AVG(amenities_score) :: numeric, 2) average_amenities_score
FROM house_listings h
JOIN amenities a ON h.amenities_id = a.amenities_id
GROUP BY h.property_type
ORDER BY average_amenities_score DESC;


-- Top 10 hosts with highest average review score of 'A'
SELECT hl.host_id, COUNT(r.average_review_score) AS total_times_highest_score, h.host_name
FROM house_listings hl
JOIN hosts h ON hl.host_id = h.host_id
JOIN review r on hl.review_id = r.review_id
WHERE r.average_review_score = 'A'
GROUP BY hl.host_id, h.host_name 
ORDER BY total_times_highest_score DESC
LIMIT 10;
