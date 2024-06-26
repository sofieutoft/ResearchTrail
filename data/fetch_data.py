import requests
import xml.etree.ElementTree as ET

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
        entry_data = {
            "id": entry.find("{http://www.w3.org/2005/Atom}id").text,
            "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
            "published": entry.find("{http://www.w3.org/2005/Atom}published").text,
        }
        entries.append(entry_data)
    return entries
