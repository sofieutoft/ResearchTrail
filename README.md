# arXiv Recommendation System

This project fetches machine learning papers from the arXiv API, processes the data, and provides a recommendation system to suggest related papers based on content similarity. The aim of this project is to streamline the literature review process.


### File Details

- **`app.py`**: Main application logic.
- **`requirements.txt`**: Project dependencies.
- **`README.md`**: Project documentation and setup instructions.
- **`config.py`**: Configuration settings.
- **`data/`**: Contains modules for data fetching, preprocessing, database operations, and recommendations.
  - **`fetch_data.py`**: Functions for fetching data from the arXiv API.
  - **`preprocess.py`**: Text preprocessing functions.
  - **`database.py`**: Database connection and operations.
  - **`recommend.py`**: Recommendation system functions.
- **`templates/`**: HTML templates for rendering web pages.
  - **`index.html`**: Template to display the list of papers.
  - **`recommend.html`**: Template to display recommended papers.
- **`static/css/`**: CSS stylesheets for the web application.
  - **`styles.css`**: Stylesheet for the web application.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/arxiv-recommendation-system.git
    cd arxiv-recommendation-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

## Usage

1. The home page (`index.html`) displays a list of machine learning papers fetched from the arXiv API.
2. Click on any paper title to view a list of recommended papers similar to the selected paper.
3. The recommendations are based on the content similarity of the paper summaries.

## Dependencies

- Flask==2.0.2
- requests==2.26.0
- SQLAlchemy==1.4.25
- pandas==1.3.3
- nltk==3.6.3
- scikit-learn==0.24.2

Make sure to install these dependencies using the `requirements.txt` file provided.


![Style Status](https://github.com/sofieutoft/arXivproject/actions/workflows/style.yaml/badge.svg)
