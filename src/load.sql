----------------- BULK Loading from csv files -----------------------------------------

COPY amenities FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/amenities.csv' DELIMITER ',' CSV HEADER;

COPY hosts FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/host_v2.csv' DELIMITER ',' CSV HEADER;

COPY neighbourhood FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/neighbourhood.csv' DELIMITER ',' CSV HEADER;

COPY locations FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/location_v2.csv' DELIMITER ',' CSV HEADER;

COPY review FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/review.csv' DELIMITER ',' CSV HEADER;

COPY house_listings FROM '/Users/jaskirat/University_at_Buffalo/courses/dmql/dmql_project/phase2/data_tables/house_listings_v2.csv' DELIMITER ',' CSV HEADER;
