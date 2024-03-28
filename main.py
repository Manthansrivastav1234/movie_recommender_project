import streamlit as st
import pickle
import pandas as pd
import requests
def recommend(movie):
    idx = movies[movies['original_title'] == movie].index[0]
    similar_movie_index = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommended_movie_poster =[ ]
    for i in similar_movie_index:
        movieid = movies.iloc[i[0]]['movie_id']
        recommended_movie_poster.append(fetch_poster(movieid))
        recommend_movies.append(movies.iloc[i[0]]['original_title'])
    return recommend_movies,recommended_movie_poster

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



movie_dic = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dic)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'movie you have watched',
    movies['original_title'].values
)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



