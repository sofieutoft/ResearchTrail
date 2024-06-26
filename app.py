import requests
import sqlalchemy as db
import pandas as pd
import xml.etree.ElementTree as ET
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request

# Download NLTK stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Flask app setup
app = Flask(__name__)


# Send the GET request
def get_request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except Exception as err:
        return f"An error occurred: {err}"


# Extract data
def extract_data(root):
    entries = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        entry_data = {
            "id": entry.find("{http://www.w3.org/2005/Atom}id").text,
            "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
            "published":
                entry.find("{http://www.w3.org/2005/Atom}published").text,
        }
        entries.append(entry_data)
    return entries

# Function to preprocess text
def preprocess_text(text):
    # Remove punctuation and lower the text
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)


# Function to connect to database and store data
def connect(data):
    df = pd.DataFrame(data)
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

# Get response and process data
response = get_request(url, parameters)
root = ET.fromstring(response.content)
data = extract_data(root)

# Preprocess the summaries
data = pd.DataFrame(data)
data['clean_summary'] = data['summary'].apply(preprocess_text)

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['clean_summary'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(paper_id, cosine_sim=cosine_sim):
    # Get the index of the paper that matches the paper_id
    idx = data.index[data['id'] == paper_id].tolist()[0]
    # Get the pairwise similarity scores of all papers with that paper
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the papers based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the indices of the 5 most similar papers
    sim_scores = sim_scores[1:6]
    # Get the paper indices
    paper_indices = [i[0] for i in sim_scores]
    # Return the titles of the most similar papers
    return data['title'].iloc[paper_indices]

@app.route('/')
def index():
    engine = db.create_engine('sqlite:///arXiv.db')
    with engine.connect() as connection:
        query_result = connection.execute(
            db.text("SELECT * FROM arXivPapers;")).fetchall()
        data = pd.DataFrame(query_result, columns=query_result[0].keys())
    return render_template('index.html', data=data)

@app.route('/recommend', methods=['GET'])
def recommend():
    paper_id = request.args.get('id')
    recommendations = get_recommendations(paper_id)
    return render_template('recommend.html', paper_id=paper_id, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
