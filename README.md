# DMDD_Project_WorldEnergy
Database Project: Used Python &amp; Mysql. Twitter Scraping: Performed Data Gathering, Munging, Cleaning and Normalization. 

Content of the Project: The final project folder has following contents:

1- Source of Data: https://www.bp.com/en/global/corporate/energy-economics/statistical- review-of- world-energy/downloads.html
2- Code Files: The code files folder has three python scripts:
i) twitter_api.py : This script file scraps twitter data and insert the related data in the respective tables.
ii) insertDataDomain.py : This script is responsible for creating domain-related tables and inserting data in those tables from the dataset.
iii) dataVisualization.py : This script file is responsible for data visualization of the domain model into pie charts and bar graphs.

3- ER Diagram : Contains ER Diagram which shows the relation between all the domain and twitter tables along with the type of relations they are associated with.
4- Data Set : Contains all refactored data downloaded from the web, along with the data used for data domain insertion and visualization.
5- SQL Queries: Contains all the SQL queries and all the use cases from assignments #2- #4(includes creation, insertion, and deletion of tables and data along with joins and views).
6- DataBasePicture: This folder has all the consolidated snippets of the database & tables created, snippets of Use Cases, and snippets of visualization performed on the Database.
About the Project:

World's Energy Consumption FY- 2021
This project is a data representation of Energy Consumption by Country and their geographical groupings. It focuses on the types of Energy consumption along with the quantity of energy consumption and how it is changing over time. It has data on countries & continents with their per capita energy (Oil, Gas & Coal) consumption and CO2 Emissions. The database also contains the source of renewable energies (solar, wind, geothermal) along with their consumption.
ER Diagram & Description:
The ER Diagram attached is a graphical representation of the database that has been implemented for the project- World Energy. This is a blueprint of how data has been stored in form of Relations between each table.
The data representation of Energy Consumption by Country and their geographical groupings focuses on types of Energy consumption along with the quantity of energy consumption and how it is changing over time. It also consists of CO2 emissions by developed and developing nations. The database also contains the data for renewable energies i.e., Solar and Wind Energies along with the consumption.
 
Explanation of some of the Design Decisions:
 CountryAndCode table has the Geographical location mapped with the countries and each country has a unique id associated with it, this acts as the primary key in this table and acts as a foreign key for others.
 The DB also consists of 4 tables which are extracted from Twitter. The data extracted from Twitter gives information about twitter tweets on Wind Energy, CO2 Emissions, Solar Energy and Renewable Energy.
 The extracted tweeter tables are further related to the main CountryAndCodeTable which has location as their foreign key. By the help of the foreign key, it’d be easier to extract hashtags and
tweets related to the particular ‘Energy Table’.
 TwitterDataTables (WorldOnRenewableEnery, C02Emission) has information on the user posted,
location, tweet created at what time, description, tweet, and the User Created Info. A user can come, and extract data based on keywords such as – ‘CO2Emission’, ‘GreenEnergy’, ‘RenewableEnergy’ etc.
 With the help of the foreign key ‘idCountryAndCode’ a user will be able to retrieve data from the ‘Primary Energy Consumption Per Capita’ of a country, the CO2 Emission of Geographical areas, and also Renewable Energy Consumption By Fuel Type. The Renewable Energy Generation and consumption of a particular area are also being retrieved by the same key.
