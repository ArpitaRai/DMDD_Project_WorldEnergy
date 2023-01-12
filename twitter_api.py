import datetime
import time
import tweepy
import configparser
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import geocoder
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import csv
import datetime, time


#------------------------------------------------------------------------------------------
#read config file
#------------------------------------------------------------------------------------------

config= configparser.ConfigParser()
config.read('config.ini')
api_key=config['twitter']['api_key']
api_key_secret= config['twitter']['api_key_secret']

access_token= config['twitter']['access_token']
access_token_secret= config['twitter']['access_token_secret']

#------------------------------------------------------------------------------------------
#authentication check
#------------------------------------------------------------------------------------------

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth) 
try:
    api.verify_credentials()
    print("Authentication SUCCESSFUL!!!")
except:
    print("Error during authentication")

#------------------------------------------------------------------------------------------
#tweets on wind energy
#------------------------------------------------------------------------------------------
now = datetime.date.today()
date_since = datetime.datetime.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
print (date_since)
columns = ['User','User Created At', 'Description', 'Tweet Created At' , 'Location','Tweet']
data= []
new_search= "WindEnergy"
num_tweets =100
tweets = tweepy.Cursor(api.search_tweets, 
              q=new_search,
              lang="en",
              until=date_since).items(num_tweets)
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.user.created_at, tweet.user.description, tweet.created_at,
    tweet.user.location, tweet.text])

df=pd.DataFrame(data, columns=columns)

print(df )
df.to_csv('WorldOnWindEnergy.csv', sep=',', encoding='utf-8')

# -------------------------------------------------------------------------------------------------
#tweets on solar energy
# -------------------------------------------------------------------------------------------------

columns = ['User','User Created At','Description', 'Tweet Created At' ,'Location','Tweet']
data= []
new_search= "SolarEnergy"
tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              until=date_since).items(num_tweets)
for tweet in tweets:
    data.append([ tweet.user.screen_name, tweet.user.created_at,tweet.user.description, tweet.created_at,
    tweet.user.location, tweet.text])

df=pd.DataFrame(data, columns=columns)

print(df )
df.to_csv('WorldOnSolarEnergy.csv', sep=',', encoding='utf-8')

# -------------------------------------------------------------------------------------------------
#tweets on CO2 Emission
#--------------------------------------------------------------------------------------------------

columns = ['User','User Created At','Description', 'Tweet Created At' ,'Location','Tweet']
data= []
new_search= "#CO2"
tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              until=date_since).items(num_tweets)
for tweet in tweets:
    data.append([ tweet.user.screen_name, tweet.user.created_at,tweet.user.description, tweet.created_at,
    tweet.user.location, tweet.text])

df=pd.DataFrame(data, columns=columns)

print(df )
df.to_csv('WorldOnCO2Emission.csv', sep=',', encoding='utf-8')
#-------------------------------------------------------------------------------------------------
#tweets on renewable energy
#-------------------------------------------------------------------------------------------------

columns = ['User','User Created At','Description', 'Tweet Created At' ,'Location','Tweet']
data= []
new_search= "#renewableenergy"
tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              until=date_since).items(num_tweets)
for tweet in tweets:
    data.append([ tweet.user.screen_name, tweet.user.created_at,tweet.user.description, tweet.created_at,
    tweet.user.location, tweet.text])

df=pd.DataFrame(data, columns=columns)

print(df )
df.to_csv('WorldOnRenewableEnergy.csv', sep=',', encoding='utf-8')

#-------------------------------------------------------------------------------------------------
#tweets on climate change
#-------------------------------------------------------------------------------------------------

columns = ['User','User Created At','Description', 'Tweet Created At' ,'Location','Tweet']
data= []
new_search= "#climatechange"
tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              until=date_since).items(num_tweets)
for tweet in tweets:
    data.append([ tweet.user.screen_name, tweet.user.created_at,tweet.user.description, tweet.created_at,
    tweet.user.location, tweet.text])

df=pd.DataFrame(data, columns=columns)

print(df )
df.to_csv('WorldOnClimateChange.csv', sep=',', encoding='utf-8')

#-------------------------------------------------------------------------------------------------
# location wise CO2 tweets- INDIA
# convert to a DataFrame and keep only relevant columns
# -------------------------------------------------------------------------------------------------

df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'CO2 near:"India" within:1000km').get_items(), 100))[['date', 'content']]

df_city.to_csv('CO2India.csv', sep=',', encoding='utf-8')

#-------------------------------------------------------------------------------------------------
# location wise CO2 tweets- CHINA
# convert to a DataFrame and keep only relevant columns
# -------------------------------------------------------------------------------------------------

df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'CO2 near:"China" within:1000km').get_items(), 100))[['date', 'content']]

df_city.to_csv('CO2China.csv', sep=',', encoding='utf-8')

#-------------------------------------------------------------------------------------------------
# location wise CO2 tweets- USA
# convert to a DataFrame and keep only relevant columns
# -------------------------------------------------------------------------------------------------


df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'CO2 near:"USA" within:1000km').get_items(), 100))[['date', 'content']]

df_city.to_csv('CO2USA.csv', sep=',', encoding='utf-8')

#-------------------------------------------------------------------------------------------------
# location wise CO2 tweets- USA
# convert to a DataFrame and keep only relevant columns
# -------------------------------------------------------------------------------------------------

df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'CO2 near:"Europe" within:1000km').get_items(), 100))[['date', 'content']]

df_city.to_csv('CO2Eu27.csv', sep=',', encoding='utf-8')
#-------------------------------------------------------------------------------------------------
#Trending Tweets - USA
# -------------------------------------------------------------------------------------------------

def get_trends(api, loc):
    # Object that has location's latitude and longitude.
    g = geocoder.osm(loc)

    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]["woeid"])
    # trends = api.get_place_trends(1)
    return trends[0]["trends"]

if __name__ == "__main__":
    loc = "USA"
    trends = get_trends(api, loc)

tweets_data = [] #initialize master list to hold our ready tweets

tweets = pd.DataFrame(
        [ t.values() for t in trends], 
        columns = trends[0].keys())
print(tweets)

tweets.to_csv('TrendingUSA.csv')

#-------------------------------------------------------------------------------------------------
#Trending Tweets - India
# -------------------------------------------------------------------------------------------------

def get_trends(api, loc):
    # Object that has location's latitude and longitude.
    g = geocoder.osm(loc)

    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]["woeid"])
    # trends = api.get_place_trends(1)
    return trends[0]["trends"]

if __name__ == "__main__":
    loc = "India"
    trends = get_trends(api, loc)

tweets_data = [] #initialize master list to hold our ready tweets

tweets = pd.DataFrame(
        [ t.values() for t in trends], 
        columns = trends[0].keys())
print(tweets)

tweets.to_csv('TrendingIndia.csv')

#-------------------------------------------------------------------------------------------------
# MySql DB Connection
# -------------------------------------------------------------------------------------------------


database = MySQLdb.connect (host="localhost" , user="root" , password="9125arpitarai" ,db="DMDDWorldEnergy")
cursor = database.cursor()

#-------------------------------------------------------------------------------------------------
#MySql Wind Energy Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


windEnergy = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`WorldOnWindEnergy` (`UserName` VARCHAR(45) NULL,`UserCreatedAt` VARCHAR(45) NULL,`Description` VARCHAR(400) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`Tweet` VARCHAR(5000) NULL)"
cursor.execute(windEnergy)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`WorldOnWindEnergy`")

with open('WorldOnWindEnergy.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[3],row[4],row[5],row[6])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`WorldOnWindEnergy` (`UserName`,`UserCreatedAt`,`Description`,`TweetCreatedAt`,`Location`,`Tweet`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql Solar Energy Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


solarEnergy = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`WorldOnSolarEnergy` (`UserName` VARCHAR(45) NULL,`UserCreatedAt` VARCHAR(45) NULL,`Description` VARCHAR(400) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`Tweet` VARCHAR(500) NULL)"
cursor.execute(solarEnergy)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`WorldOnSolarEnergy`")

with open('WorldOnSolarEnergy.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[3],row[4],row[5],row[6])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`WorldOnSolarEnergy` (`UserName`,`UserCreatedAt`,`Description`,`TweetCreatedAt`,`Location`,`Tweet`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql Renewable Energy Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


renewableEnergy = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`WorldOnRenewableEnergy` (`UserName` VARCHAR(45) NULL,`UserCreatedAt` VARCHAR(45) NULL,`Description` VARCHAR(400) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`Tweet` VARCHAR(5000) NULL)"
cursor.execute(renewableEnergy)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`WorldOnRenewableEnergy`")

with open('WorldOnRenewableEnergy.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[3],row[4],row[5],row[6])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`WorldOnRenewableEnergy` (`UserName`,`UserCreatedAt`,`Description`,`TweetCreatedAt`,`Location`,`Tweet`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2Emission Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


cO2Emission = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2Emission` (`UserName` VARCHAR(45) NULL,`UserCreatedAt` VARCHAR(45) NULL,`Description` VARCHAR(400) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`Tweet` VARCHAR(5000) NULL)"
cursor.execute(cO2Emission)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2Emission`")

with open('WorldOnCO2Emission.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[3],row[4],row[5],row[6])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2Emission` (`UserName`,`UserCreatedAt`,`Description`,`TweetCreatedAt`,`Location`,`Tweet`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql Climate Change Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


climateChange = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`ClimateChange` (`UserName` VARCHAR(45) NULL,`UserCreatedAt` VARCHAR(45) NULL,`Description` VARCHAR(400) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`Tweet` VARCHAR(5000) NULL)"
cursor.execute(climateChange)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`ClimateChange`")

with open('WorldOnClimateChange.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[3],row[4],row[5],row[6])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`ClimateChange` (`UserName`,`UserCreatedAt`,`Description`,`TweetCreatedAt`,`Location`,`Tweet`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2China Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


co2China = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2China` (`Date` VARCHAR(45) NULL,`Content` VARCHAR(5000) NULL)"
cursor.execute(co2China)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2China`")

with open('CO2China.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2China` (`Date`,`Content`) VALUES (%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2CEu27 Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


co2Eu27 = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2Eu27` (`Date` VARCHAR(45) NULL,`Content` VARCHAR(1000) NULL)"
cursor.execute(co2Eu27)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2Eu27`")

with open('CO2Eu27.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2Eu27` (`Date`,`Content`) VALUES (%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2India Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


co2India = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2India` (`Date` VARCHAR(45) NULL,`Content` VARCHAR(5000) NULL)"
cursor.execute(co2India)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2India`")

with open('CO2India.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2India` (`Date`,`Content`) VALUES (%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2USA Creation and Data Insertion
# -------------------------------------------------------------------------------------------------

co2usa = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2USA` (`Date` VARCHAR(45) NULL,`Content` VARCHAR(5000) NULL)"
cursor.execute(co2usa)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2USA`")

with open('CO2USA.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2USA` (`Date`,`Content`) VALUES (%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql CO2USA Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


co2usa = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`CO2USA` (`Date` VARCHAR(45) NULL,`Content` VARCHAR(5000) NULL)"
cursor.execute(co2usa)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`CO2USA`")

with open('CO2USA.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`CO2USA` (`Date`,`Content`) VALUES (%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()


#-------------------------------------------------------------------------------------------------
#MySql Trending in India Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


trendingIndia = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`TrendingIndia` (`Name` VARCHAR(45) NULL,`URL` VARCHAR(500) NULL, `Query` VARCHAR(900) NULL, `TweetVolume` VARCHAR(100) NULL)"
cursor.execute(trendingIndia)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`TrendingIndia`")

with open('TrendingIndia.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[4],row[5])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`TrendingIndia` (`Name`,`URL`,`Query`,`TweetVolume`) VALUES (%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

#-------------------------------------------------------------------------------------------------
#MySql Trending in USA Creation and Data Insertion
# -------------------------------------------------------------------------------------------------


trendingUsa = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`TrendingUSA` (`Name` VARCHAR(45) NULL,`URL` VARCHAR(500) NULL, `Query` VARCHAR(900) NULL, `TweetVolume` VARCHAR(100) NULL)"
cursor.execute(trendingUsa)
cursor.execute("DESCRIBE `DMDDWorldEnergy`.`TrendingUSA`")

with open('TrendingUSA.csv') as csv_file:
    csvFile=csv.reader(csv_file,delimiter=',')
    allValue=[]
    for row in csvFile:
        value=(row[1],row[2],row[4],row[5])
        allValue.append(value)

 
insert_query = "INSERT INTO `DMDDWorldEnergy`.`TrendingUSA` (`Name`,`URL`,`Query`,`TweetVolume`) VALUES (%s,%s,%s,%s)"
cursor.executemany(insert_query,allValue)
database.commit()

# -------------------------------------------------------------------------------------------------
# Below is a code which extracts all tweets of a paticular user
#---------------------------------------------------------------------------------------------------------------------------------------    
    
user = "UN_Energy"   
tweets = api.user_timeline(screen_name=user, 
                           count=20,
                           include_rts = True,
                           tweet_mode = 'extended')
columns = ['UserID','Username', 'Tweet', 'TweetCreatedAt', 'Location', 'UserCreatedAt' ]
data = []
for tweet in tweets:
    data.append([tweet.id_str, tweet.user.screen_name, tweet.full_text, tweet.created_at, tweet.user.location, tweet.user.created_at])

df = pd.DataFrame(data, columns = columns)

print(df)
userData = "CREATE TABLE IF NOT EXISTS `DMDDWorldEnergy`.`UserData` (`UserID` VARCHAR(45) NULL,`UserName` VARCHAR(45) NULL,`Tweet` VARCHAR(800) NULL,`TweetCreatedAt` VARCHAR(100) NULL,`Location` VARCHAR(100) NULL,`UserCreatedAt` VARCHAR(500) NULL)"
cursor.execute(userData)
for i,row in df.iterrows():
            sql = "INSERT INTO DMDDWorldEnergy.UserData VALUES (%s,%s,%s,%s,%s,%s)"
            print(tuple(row))
            cursor.execute(sql, tuple(row))
database.commit()

result = cursor.fetchall()
for i in result:
    print(i)


    