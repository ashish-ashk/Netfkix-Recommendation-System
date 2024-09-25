import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

movies_df = pd.read_csv('movies_df.csv')
movies_sim = np.load('movies_sim.npz')
movies_sim = movies_sim['m']

tv_show = pd.read_csv('tv_show.csv')
tv_sim = np.load('tv_sim.npz')
tv_sim = tv_sim['t']

# Function to recommend the movies
def recommend(title):
    pass

# Movies and TV shows checkpoints
movie_list = sorted(movies_df['title'].tolist() + tv_show['title'].tolist())

####################################################################
#streamlit
##################################################################

st.header('Netflix Movie Recommendation System ')
lottie_coding = load_lottiefile("netflix-logo.json")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",height=220
)
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    # display table
    st.subheader("Top 10 Recommended Movies")
    st.dataframe(data=recommended_movie_names[['title', 'country', 'genres', 'description', 'release_year', 'cast']])
