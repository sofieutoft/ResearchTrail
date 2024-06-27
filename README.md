# arXiv Recommendation System

This project fetches machine learning papers from the arXiv API, processes the data, and provides a recommendation system to suggest related papers based on content similarity. The aim of this project is to streamline the literature review process.

## File Details

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
  - **`style2.css`**: Another stylesheet for the web application.
- **`Dockerfile`**: Docker configuration file for containerization.
- **`.dockerignore`**: File to specify Docker files and directories to ignore.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/sofieutoft/arXivproject.git
    cd arXivproject
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r ./arXivproject/requirements.txt
    ```

4. Run the application locally (must update ```app.run(host='0.0.0.0', port=1024)``` in app.py to correct host & port):
    ```bash
    python3 ./arXivproject/app.py
    ```

5. Open your browser and go to `http://127.0.0.1:1024/` to view the application (depends on host & port).

## Docker Deployment

To deploy using Docker, follow these steps:

1. Build the Docker image:
    ```bash
    docker build -t arxiv-recommendation-system .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 1024:1024 arxiv-recommendation-system
    ```

3. Open your browser and go to `http://localhost:1024/` to view the application.

## Usage

1. The home page (`index.html`) displays a list of machine learning papers fetched from the arXiv API.
2. Click on any paper title to view a list of recommended papers similar to the selected paper.
3. The recommendations are based on the content similarity of the paper summaries.

## Dependencies

- Flask
- requests
- coverage
- SQLAlchemy
- pandas
- nltk
- scikit-learn

Make sure to install these dependencies using the `requirements.txt` file provided.

![Style Status](https://github.com/sofieutoft/arXivproject/actions/workflows/style.yaml/badge.svg)
