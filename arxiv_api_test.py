import requests
import sqlalchemy as db
import pandas as pd
import xml.etree.ElementTree as ET


# send the GET request
def request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return "Request successful!"
        # print(response.text)
    except Exception as err:
        string = "An error occurred: " + str(err)
        return string

# extract data
def extract_data(root):
    entries = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        entry_data = {
            "id": entry.find("{http://www.w3.org/2005/Atom}id").text,
            "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
            "published": entry.find("{http://www.w3.org/2005/Atom}published").text,
        }
        entries.append(entry_data)
    return entries

def connect(dict):
    df = pd.DataFrame.from_dict(dict)

    engine = db.create_engine('sqlite:///arXiv.db')

    df.to_sql('arXivPapers', con=engine, if_exists='replace', index=False)

    with engine.connect() as connection:
        query_result = connection.execute(
            db.text("SELECT title FROM arXivPapers;")).fetchall()
        print(pd.DataFrame(query_result))


# URL for arXiv API
url = "http://export.arxiv.org/api/query"

# parameters for the search query
parameters = {
    "search_query": "all:machine learning",
    "start": 0,
    "max_results": 5
}

# get response
request(url, parameters)

# parse XML response
root = ET.fromstring(response.content)
dictionary = extract_data(root)

connect(dictionary)

