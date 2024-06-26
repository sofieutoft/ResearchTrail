from flask import Flask, render_template, request
from config import ARXIV_API_URL
from data.fetch_data import get_request, extract_data
from data.preprocess import preprocess_text
from data.database import connect
from data.recommend import get_recommendations
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    engine = db.create_engine(DATABASE_URI)
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM arXivPapers;")).fetchall()
        data = pd.DataFrame(query_result, columns=query_result[0].keys())
    return render_template('index.html', data=data)

@app.route('/recommend', methods=['GET'])
def recommend():
    paper_id = request.args.get('id')
    recommendations = get_recommendations(data, paper_id)
    return render_template('recommend.html', paper_id=paper_id, recommendations=recommendations)

if __name__ == '__main__':
    # Fetch and process data
    parameters = {
        "search_query": "all:machine learning",
        "start": 0,
        "max_results": 5
    }
    response = get_request(ARXIV_API_URL, parameters)
    data = extract_data(response.content)
    data = pd.DataFrame(data)
    data['clean_summary'] = data['summary'].apply(preprocess_text)

    # Connect to database and store data
    connect(data)

    # Run the Flask application
    app.run(debug=True)
