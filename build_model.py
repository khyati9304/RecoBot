import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset
movies = pd.read_csv("movies.csv")

# Handle missing values
movies["genres"] = movies["genres"].fillna("")
movies["overview"] = movies["overview"].fillna("")

# Combine genres and overview
movies["tags"] = movies["genres"] + " " + movies["overview"]

# Convert text into numerical TF-IDF vectors
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["tags"])

# Calculate cosine similarity between all movies
similarity = cosine_similarity(tfidf_matrix)

# Save similarity matrix
with open("similarity.pkl", "wb") as file:
    pickle.dump(similarity, file)

print("similarity.pkl created successfully!")
print("Similarity matrix shape:", similarity.shape)
