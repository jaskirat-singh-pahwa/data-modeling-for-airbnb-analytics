PROJECT AIM:
The aim of the project was to create a relational database for a house listing dataset for Airbnb to deal with the inherent issues like redundacny, anomalies and poor linking between the entities.


DATASET:
The data accumulation phase of the project included gathering house listing dataset in a single flat file. This dataset was further aided with two other dataset, namely, review and neighbourhood. These dataset are also present as a flat files.


DATA NORMALIZATION:
In order to deal with the above issues with the dataset we created a relational database with 6 data tables-
location 
neighbourhood
host
house_listing
amenities
review


DATA CLEANING:
We performed data cleaning on the orginal dataset and segregated the original data into the above tables to remove data redundancy and anomalies. As part of the data cleaning process,
we have chosen the top most popular amenities in the dataset and fetches different combinations of each of the amenities and assigned scores to each combination to aid the decision making of the customer.
In the review table we have assigned letter grades to the review score that were assigned to each of the listing and further evaluated an average overall grade based on the individual grades.


QUERIES:
Once the tables are created we have defined the relationship between the table.
First we inserted the data using BULK LOAD queries and ran certain CRUD operations like CREATE, INSERT, DELETE, UPDATE and SELECT queries. The same has been mentioned in the doc.


WEB UI:
Finally, we have created a UI where we can run the queries that are mentioned in the document and this would generate the output as well as the graphical visualization of the output result of the queries.

To run the code:
We need to go inside src directory and we can type the following command in the terminal:
	streamlit run streamlit_dmql.py

	make sure we have these two libraries:
	pip3 install streamlit
	python3 -m pip install psycopg2-binary
	