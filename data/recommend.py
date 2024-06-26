from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_recommendations(data, paper_id):
    # Convert text data to TF-IDF features
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['clean_summary'])

    # Compute cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

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
