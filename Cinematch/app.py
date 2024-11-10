import streamlit as st
import pandas as pd
import pickle
import requests


movie_list = pickle.load(open('movies.pkl','rb'))
movie_list1=movie_list['title'].values

from streamlit_lottie  import st_lottie
import json
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

similarity=pickle.load(open('similarity.pkl','rb'))
import streamlit as st

#def fetch_poster(movie_id):
    #response=requests.get('https://api.themoviedb.org/3/movie/{}?api_keyedc688a3df587c53117a1f42b2dd26c0&language=en-US'.format(movie_id))
    #data=response.json()
    #return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=edc688a3df587c53117a1f42b2dd26c0&language=en-US')
    data = response.json()
    if 'poster_path' in data:
        return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    else:
        return ''


def recommend(movie):
    movie_index=movie_list[movie_list['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True ,key=lambda x:x[1])[1:6]

    recommended_movies_posters=[]
    recommended_movies=[]
    for i in movies_list:
        movie_id=movie_list.iloc[i[0]]['movie_id']
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movie_list.iloc[i[0]]['title'])
    return recommended_movies,recommended_movies_posters
rad=st.sidebar.radio("Navigation",["HOME","Recommendations","About Us"])


if rad=="HOME":
    st.image("logo.jpeg")
    lottie1=load_lottiefile("lf20_CTaizi.json")
    st_lottie(lottie1,height=600,width=600)

if rad=="Recommendations":
    st.image("logo.jpeg")
    lottie2=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_DW2u8OuYdH.json")
    st_lottie(lottie2,height=100,width=100)


    selected_movie_name = st.selectbox(
    'SELECT ONE OF YOUR FAVOURITE MOVIE',movie_list1)

    if st.button('RECOMMEND'):

        
        
        #st.write(selected_movie_name)
        
        names, posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(posters[0], caption=  names[0], width=150)
        with col2:
            st.image(posters[1], caption=  names[1], width=150)
        with col3:
            st.image(posters[2], caption= names[2], width=150)
        with col4:
            st.image(posters[3], caption= names[3], width=150)
        with col5:
            st.image(posters[4], caption=names[4], width=150)

if rad=="About Us":
    st.image("logo.jpeg")
    if st.button('DOCUMENT'):
        st.subheader("Welcome to our movie recommendation website, where we help you discover the perfect movie for your mood. Our machine learning algorithm analyzes over 5000 movies to provide you with the most accurate recommendations. Whether you're in the mood for an action-packed thriller or a heartwarming romance, we've got you covered. So sit back, relax, and let us take care of the rest. With our website, you'll never have to spend hours scrolling through Netflix again. Enjoy your movie!")

    if st.button('AUDIO'):
        lottie4=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_pzrstZ.json")
        st_lottie(lottie4,height=400,width=650)

        st.audio("aud.mp3.crdownload")
    
   
    



