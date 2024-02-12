---------------------------------- CREATE TABLE QUERIES ----------------------------------------------------
CREATE TABLE IF NOT EXISTS amenities (
	amenities_id INTEGER PRIMARY KEY,
	amenities_description TEXT NOT NULL,
	amenities_score INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS hosts (
	host_id INTEGER PRIMARY KEY,
	host_name TEXT,
	host_since TEXT,
	host_location TEXT,
	host_about TEXT,
	host_response_time TEXT,
	host_acceptance_rate VARCHAR(10),
	host_is_superhost VARCHAR(10),
	host_neighbourhood VARCHAR(30),
	host_verifications TEXT
);


CREATE TABLE IF NOT EXISTS neighbourhood (
	neighbourhood_id INTEGER PRIMARY KEY,
	neighbourhood TEXT NOT NULL,
	neighbourhood_cleansed TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS locations (
	zipcode INTEGER PRIMARY KEY,
	street TEXT NOT NULL,
	neighbourhood_id INTEGER NOT NULL,
	FOREIGN KEY (neighbourhood_id) REFERENCES neighbourhood(neighbourhood_id)
);


CREATE TABLE IF NOT EXISTS review (
	review_id INTEGER PRIMARY KEY,
	review_rating_grade VARCHAR(5) NOT NULL,
	review_accuracy_grade VARCHAR(5) NOT NULL,
	review_cleanliness_grade VARCHAR(5) NOT NULL,
	review_communication_grade VARCHAR(5) NOT NULL,
	average_review_score VARCHAR(5) NOT NULL
);


CREATE TABLE IF NOT EXISTS house_listings (
	listing_id INTEGER PRIMARY KEY,
	listing_name TEXT NOT NULL,
	description TEXT NOT NULL,
	neighborhood_overview TEXT NOT NULL,
	zipcode INTEGER NOT NULL,
	latitude TEXT NOT NULL,
	longitude TEXT NOT NULL,
	property_type TEXT NOT NULL,
	amenities_id INTEGER NOT NULL,
	room_type TEXT NOT NULL,
	accommodates TEXT NOT NULL,
	bathrooms DOUBLE PRECISION NOT NULL,
	beds DOUBLE PRECISION NOT NULL,
	price TEXT NOT NULL,
	minimum_nights TEXT NOT NULL,
	maximum_nights TEXT NOT NULL,
	has_availability TEXT NOT NULL,
	availability_30 TEXT NOT NULL,
	availability_60 TEXT NOT NULL, 
	availability_90 TEXT NOT NULL,
	availability_365 TEXT NOT NULL,
	review_id INTEGER NOT NULL,
	host_id INTEGER NOT NULL,
	FOREIGN KEY (zipcode) REFERENCES locations(zipcode),
	FOREIGN KEY (amenities_id) REFERENCES amenities(amenities_id),
	FOREIGN KEY (review_id) REFERENCES review(review_id),
	FOREIGN KEY (host_id) REFERENCES hosts(host_id)
);
