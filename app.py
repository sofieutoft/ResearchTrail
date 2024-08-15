from flask import Flask, render_template, request, redirect, url_for
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
    search_query = request.args.get('query', 'all:machine learning')  # Default to 'all:machine learning'
    parameters = {
        "search_query": search_query,
        "start": 0,
        "max_results": 500
    }
    
    # Fetch and process data
    response = get_request(ARXIV_API_URL, parameters)
    data = extract_data(response.content)
    data = pd.DataFrame(data)
    data['clean_summary'] = data['summary'].apply(preprocess_text)
    
    # Connect to database and store data
    connect(data)
    
    # Fetch data from the database for display
    data = fetch_all_papers(engine)
    if data is None or data.empty:
        print("Data fetch failed or returned an empty DataFrame")
        return render_template('index.html', table_data=[])

    selected_columns = ['title', 'summary', 'published', 'link']
    table_data = data[selected_columns].to_dict(orient='records')
    return render_template('index.html', table_data=table_data, search_query=search_query)

@app.route('/recommend', methods=['GET'])
def recommend():
    paper_id = request.args.get('link')
    data = fetch_all_papers(engine)  

    # Validate paper_id
    if paper_id is None or paper_id not in data['link'].values:
        error_message = f"Paper with id '{paper_id}' not found."
        print(f"Error: {error_message}")
        return render_template('error.html', error_message=error_message)

    titles, links = get_recommendations(data, paper_id)
    recommendations = list(zip(titles, links))
    if not titles or not links:
        print(f"get_recommendations returned empty titles or links for paper_id: {paper_id}")
    title = data['title'][data['link'] == paper_id].values[0]
    
    return render_template('recommend.html', title=title, recommendations=recommendations)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            repo = git.Repo('/home/arXivProject/arXivproject')
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        except Exception as e:
            print(f"Error updating repository: {e}")
            return 'Failed to update repository', 500
    return 'Wrong event type', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1024, debug=True)