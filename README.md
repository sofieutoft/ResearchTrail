# arXiv Recommendation System

This project fetches research papers from the arXiv API, processes the data, and provides a recommendation system to suggest related papers based on content similarity. The aim of this project is to streamline the literature review process.

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
- **`Dockerfile`**: Docker configuration file for containerization.
- **`.dockerignore`**: File to specify Docker files and directories to ignore.

## View the Website: ResearchTrail 🥾🌳🌲
https://researchtrail.pythonanywhere.com

![Style Status](https://github.com/sofieutoft/arXivproject/actions/workflows/style.yaml/badge.svg)
