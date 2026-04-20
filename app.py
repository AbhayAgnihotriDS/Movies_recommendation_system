from flask import Flask, render_template, request
import pickle
import requests
import os
from dotenv import load_dotenv
import pandas as pd

# Load env variables
load_dotenv()

app = Flask(__name__)

# Load model files
movies = pickle.load(open("movies_recommended.pkl", "rb"))

# Ensure DataFrame (important fix)
if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

similarity = pickle.load(open("New_similarity.pkl", "rb"))

# OMDb API Key
API_KEY = os.getenv("http://www.omdbapi.com/?i=tt3896198&apikey=6a1f8d82")


# 🔹 Fetch Poster (OMDb version)
def fetch_poster(movie_title):
    if not API_KEY:
        return "https://via.placeholder.com/300x450?text=No+API+Key"

    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/300x450?text=API+Error"

        data = response.json()
        poster = data.get("Poster")

        if poster and poster != "N/A":
            return poster
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"

    except Exception as e:
        print("Poster Error:", e)
        return "https://via.placeholder.com/300x450?text=Error"


# 🔹 Recommendation Logic
def recommend(movie):
    movie = movie.lower()

    if movie not in movies['title'].str.lower().values:
        return [], []

    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:7]

    recommended_names = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title

        recommended_names.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_names, recommended_posters


# 🔹 Routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        movie = request.form.get("movie")

        if not movie:
            return render_template("index.html", error="Please enter a movie name")

        names, posters = recommend(movie)

        if not names:
            return render_template("index.html", error="Movie not found. Try another.")

        return render_template(
            "index.html",
            names=names,
            posters=posters
        )

    return render_template("index.html")


# 🔹  deployment
@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    
    if not query:
        return {"results": []}

    results = movies[movies['title'].str.lower().str.contains(query)].title.head(8).tolist()
    
    return {"results": results}


# 🔹 Run app
if __name__ == "__main__":
    app.run(debug=True)