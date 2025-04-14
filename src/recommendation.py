import os
import requests  # for api
import pandas as pd
here = os.path.dirname(__file__)
sim_df = pd.read_csv(f"{here}/../data/similarity.csv")
pro_df = pd.read_csv(f"{here}/../data/processed.csv")


def recommend(movie):
    """
    Recommend movies based on the input movie title.

    Parameters:
    movie (str): The title of the movie for which recommendations are to be made.

    This function finds the index of the given movie in the DataFrame,
    retrieves the similarity scores for that movie, and then sorts 
    the other movies based on their similarity scores. 
    It prints the titles of the top 10 recommended movies (excluding the input movie itself).
    """

    movie_index = pro_df[pro_df.title == movie].index[0]  # Getting index of the movie in processed data

    # Retrieve the similarity scores for the input movie
    distances = sim_df.loc[movie_index,:]  # Get similarity scores for the movie

    # Sort the movies based on similarity scores in descending order
    sorted_list = sorted(enumerate(distances), key=lambda item: item[1], reverse=True)

    top_ten_similar = []
    movies_poster = []
    for movie in sorted_list[1:11]:  # Skip the first one as it's the input movie itself

        movie_id = pro_df['id'][movie[0]]
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=7b135b6bce93fa89d622513b5a9b8514"
        response = requests.get(url)
        data = response.json()

        try:
            poster = "https://image.tmdb.org/t/p/w500/" + data['poster_path']

        except TypeError:
            poster = "https://as2.ftcdn.net/v2/jpg/07/95/29/45/1000_F_795294547_gaBzWLhkAYBSz1ZUIZssHhvzGzstNmHK.jpg"
        movies_poster.append(poster)

        top_ten_similar.append(pro_df['title'][movie[0]])  # append the title of the recommended movie

    return top_ten_similar, movies_poster



