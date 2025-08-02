import pandas as pd
import pickle
import streamlit as st


movie_dict = pickle.load(open('movies.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))

movies = pd.DataFrame(movie_dict)

def reccommend(name):
    index = movies[movies['title'] == name].index[0]
    distance = similarity[index]
    movies_list = sorted(list(enumerate(distance)),reverse = True , key = lambda x:x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

### UI

st.title('Movie recommender System')
selected_name = st.selectbox('Choose movie' , movies['title'].values)
if st.button('Recommend'):
    recommend_list = reccommend(selected_name)
    st.write(recommend_list)


