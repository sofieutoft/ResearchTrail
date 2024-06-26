import requests
import xml.etree.ElementTree as ET
import datetime


def get_request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except Exception as err:
        return f"An error occurred: {err}"


def extract_data(response_content):
    root = ET.fromstring(response_content)
    entries = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        full_date = entry.find("{http://www.w3.org/2005/Atom}published").text
        published_year = datetime.datetime.strptime(full_date, "%Y-%m-%dT%H:%M:%SZ").year
        
        entry_data = {
            "link": entry.find("{http://www.w3.org/2005/Atom}id").text,
            "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
            "published": published_year,
        }
        entries.append(entry_data)
    return entries
