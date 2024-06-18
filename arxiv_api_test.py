import requests

#url for arXiv API
url = http://export.arxiv.org/api/query?

#parameters for my search_query
params = {
    search_query: all:machine learning,
    start: 0,
    max_results: 5
}

#send the get request
response = requests.get(url, params=params)

#check if the request was successful
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(Request successful!)
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(fHTTP error occurred: {err})
except Exception as err:
    print(fAn error occurred: {err})
