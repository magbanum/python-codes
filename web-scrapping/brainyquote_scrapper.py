import requests
from bs4 import BeautifulSoup
import pymongo

# Function to collect slugs for webpages.


def slug_generator(string):
    URL = "https://www.brainyquote.com/{}".format(string)
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    List = []
    for item in soup.find_all('div', 'bqLn'):
        if item.a['href'].startswith('/{}/'.format(string)):
            List.append(item.a['href'])
    print("{} collected.".format(string))
    return List

# Function to collect quotes from webpages.


def get_quotes(slug, total_pages):
    quotes = []
    for page in range(1, total_pages+1):
        URL = "https://www.brainyquote.com" + slug + "_" + str(page)
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        for item in soup.find_all('div', 'grid-item'):
            if item.find('a', 'b-qt') == None:
                continue
            temp = {}
            temp['quote'] = item.find('a', 'b-qt').text
            temp['author'] = item.find('a', 'bq-aut').text
            # List comprehension to collect list of keys.
            temp['keys'] = [key.text for key in item.find_all('a', 'qkw-btn')]
            quotes.append(temp)
    return quotes

# Function to get total number of pages for each slug


def get_quotes_by_slug(slug_list):
    print("Web scrapping by slug started...")
    quotes = []
    for slug in slug_list:
        URL = "https://www.brainyquote.com" + slug
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        pagination = soup.find('ul', 'pagination')
        # Total number of pages for slug
        if pagination:
            total_pages = int(pagination.text.split()[-2])
        else:
            total_pages = 1

        quotes += get_quotes(slug, total_pages)
    print("Web scrapping Successfully completed")
    return quotes


# Collect all the web slugs in one list
slug_list = slug_generator("authors") + slug_generator("topics")

all_quotes = []
all_quotes = get_quotes_by_slug(slug_list)

# To store all quotes in MongoDB database
client = pymongo.MongoClient('your mongodb connection string')
db = client.db.quotes
try:
    db.insert_many(all_quotes)
    print("inserted {} quotes".format(len(all_quotes)))
except:
    print("an error occured while storing data to db. Process terminated.")
