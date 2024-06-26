from flask import Flask, render_template, request
from config import ARXIV_API_URL, DATABASE_URI
from data.fetch_data import get_request, extract_data
from data.preprocess import preprocess_text
from data.database import connect, fetch_all_papers
from data.recommend import get_recommendations
import pandas as pd
import sqlalchemy as db


app = Flask(__name__)
engine = db.create_engine(DATABASE_URI)


@app.route('/')
def index():
    data = fetch_all_papers(engine)
    return render_template('index.html', tables=[data.to_html()], titles=[''])


@app.route('/recommend', methods=['GET'])
def recommend():
    paper_id = request.args.get('id')
    data = fetch_all_papers(engine)  # Fetch data again to ensure it's in scope

    # Validate paper_id
    if paper_id is None or paper_id not in data['id'].values:
        error_message = f"Paper with id '{paper_id}' not found."
        return render_template('error.html', error_message=error_message)

    recommendations = get_recommendations(data, paper_id)
    return render_template(
        'recommend.html', paper_id=paper_id, recommendations=recommendations)


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
    app.run(host='0.0.0.0', port=1024)
