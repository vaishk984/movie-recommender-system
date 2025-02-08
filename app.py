import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import pickle

file_id = "https://drive.google.com/file/d/14RoniihiPwk1BsIjyHaCTeYDwuoQn9OV/view?usp=drive_link"
gdown.download(f"https://drive.google.com/uc?id={file_id}", "similarity.pkl", quiet=False)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

def fetch_poster(movie_id):
    requests.get()
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)