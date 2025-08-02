import pandas as pd
import pickle
import streamlit as st
from huggingface_hub import hf_hub_download

REPO_ID = "savagecarol/movie-recommendation-system"
BRANCH = "main"

# Download files from Hugging Face
movies_path = hf_hub_download(repo_id=REPO_ID, filename="movies.pkl", repo_type="dataset", revision=BRANCH)
similarity_path = hf_hub_download(repo_id=REPO_ID, filename="similarity.pkl", repo_type="dataset", revision=BRANCH)

# Load data
with open(movies_path, 'rb') as f:
    movie_dict = pickle.load(f)

with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movie_dict)

# Recommend function
def recommend(movie_title):
    try:
        index = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        return []

    distance = similarity[index]
    movie_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]
    recommended = [movies.iloc[i[0]].title for i in movie_list]
    return recommended

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Choose a movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("You might also like:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.warning("No recommendations found.")
