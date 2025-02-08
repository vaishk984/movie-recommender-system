import streamlit as st
import pickle
import pandas as pd
import requests
import os

# GitHub Release URL for similarity.pkl
similarity_url = "https://github.com/vaishk984/movie-recommender-system/releases/download/v1.0/similarity.pkl"
similarity_path = "similarity.pkl"

# Function to download file if it doesn't exist
def download_file(url, file_path):
    if not os.path.exists(file_path):
        print(f"Downloading {file_path} from GitHub Releases...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)

# Download similarity.pkl if missing
download_file(similarity_url, similarity_path)

# Load files
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

with open(similarity_path, "rb") as f:
    similarity = pickle.load(f)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Choose a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
