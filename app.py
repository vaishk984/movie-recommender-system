import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

# Google Drive File ID (Extracted from shareable link)
google_drive_id = "14RoniihiPwk1BsIjyHaCTeYDwuoQn9OV"
similarity_path = "similarity.pkl"

# GitHub Release URL for similarity.pkl
github_url = "https://github.com/vaishk984/movie-recommender-system/releases/download/v1.0/similarity.pkl"

# Function to download from Google Drive
def download_from_drive(drive_id, file_path):
    import gdown
    gdown.download("https://drive.google.com/uc?id=14RoniihiPwk1BsIjyHaCTeYDwuoQn9OV", "similarity.pkl", quiet=False)


# Function to download from GitHub
def download_from_github(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded {file_path} from GitHub.")
    else:
        print("Failed to download from GitHub.")

# Check if similarity.pkl exists; if not, download it
if not os.path.exists(similarity_path):
    print("Downloading similarity.pkl from Google Drive...")
    try:
        download_from_drive(google_drive_id, similarity_path)
    except Exception as e:
        print("Google Drive download failed. Trying GitHub...")
        download_from_github(github_url, similarity_path)

# Load similarity.pkl
with open(similarity_path, "rb") as f:
    similarity = pickle.load(f)

# Load movies.pkl
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

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
