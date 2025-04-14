import pandas as pd
from src.recommendation import recommend
import streamlit as st


# Custom CSS for glass-morphism with specified colors
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        h1 {
            color: #FFAAAA;
        }
        .stSelectbox {
            background: rgba(58, 190, 249, 0.2);
            backdrop-filter: blur(10px);
            padding: 10px;
            border: 1px solid #3572EF;
            border-radius: 5px;
        }
        .stSelectbox:hover {
            background: rgba(58, 190, 249, 0.3);
        }
        .stButton {
            background-color: #3ABEF9;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #3572EF;
        }
        .stDataFrame {
            border-collapse: collapse;
            width: 100%;
        }
        .stDataFrame th, .stDataFrame td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .stDataFrame th {
            background-color: #A7E6FF;
        }
    </style>
""", unsafe_allow_html=True)


# Title
st.title('Movie Recommender System')

# Load data
df = pd.read_csv('./data/processed.csv')

# Select box for movie titles
option = st.selectbox(
    'Which similar movies do you want?',
    df['title']
)

# Display selected option
st.write('You selected:', option)

# Recommendation button
if st.button('Recommend'):
    st.write(f"Here's your top ten similar movies to {option}:")
    recommended_movies, poster_path = recommend(option)
    for i in range(len(recommended_movies)):
        st.write(f"{i+1} : {recommended_movies[i]}")
        st.image(poster_path[i], caption=recommended_movies[i])





