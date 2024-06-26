# arXiv Recommendation System

This project fetches machine learning papers from the arXiv API, processes the data, and provides a recommendation system to suggest related papers based on content similarity. The aim of this project is to streamline the literature review process.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/arxiv-recommendation-system.git
    cd arxiv-recommendation-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
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

## Project Structure

- `app.py`: Main application file.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.
- `templates/`: HTML templates for the web application.
- `static/css/`: CSS stylesheets for the web application.


![Style Status](https://github.com/sofieutoft/arXivproject/actions/workflows/style.yaml/badge.svg)
