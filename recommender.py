import streamlit as st
import pandas as pd
import pickle

# Load data
movies = pd.read_csv('movies.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommender function
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found. Try another."]
    
    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Streamlit UI
st.set_page_config(page_title="RecoBot", layout="centered")
st.title("🎬 RecoBot – Movie Recommender")
st.markdown("Get top 5 similar movie recommendations based on what you like!")

selected_movie = st.selectbox("Pick a movie:", movies['title'].values)

if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend(selected_movie)
        st.success("Here are your recommendations:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"**{i}.** {movie}")
