import os.path
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

here = os.path.dirname(__file__)

try:
    df = pd.read_csv(f"{here}/../data/processed.csv")
except FileNotFoundError:
    print("Processed file not found. Please check the path!")

df.dropna(subset=['tags'], inplace=True)
cvectorizer = CountVectorizer(max_features=5000, stop_words='english')
vectors = cvectorizer.fit_transform(df['tags'])
vectors = vectors.toarray()  # convert vectors to numpy array since it is object
similarity = cosine_similarity(vectors)
sim_df = pd.DataFrame(similarity)
sim_df.to_csv(fr"{here}/../data/similarity.csv", index=False)
