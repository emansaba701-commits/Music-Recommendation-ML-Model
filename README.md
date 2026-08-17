# 🎵 Music Recommendation System

A **content-based music recommendation system** built using Python and Machine Learning techniques. The system recommends songs that are similar to a user's selected song by analyzing song lyrics and calculating the similarity between songs.

## 🚀 Features

* 🎧 Select a song from the available dataset
* 🤖 Generate the **top 5 similar song recommendations**
* 📝 Analyze song lyrics using **TF-IDF**
* 📊 Calculate song similarity using **Cosine Similarity**
* 🖥️ Interactive frontend built with **Streamlit**
* 📦 Uses saved similarity and dataset files for fast recommendations

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* Streamlit
* Pickle

## ⚙️ How It Works

1. Song lyrics are cleaned and preprocessed.
2. Text is tokenized and stemmed using NLTK.
3. TF-IDF converts the lyrics into numerical feature vectors.
4. Cosine similarity measures how similar the songs are.
5. When a user selects a song, the system finds the most similar songs.
6. The top 5 recommendations are displayed through the Streamlit interface.

The model was developed using a dataset containing **57,650 songs**, with a 5,000-song sample used for the recommendation system.

## 📁 Project Files

* `app.py` — Streamlit frontend and recommendation logic
* `df.pkl` — Processed song dataset
* `similarity.pkl` — Precomputed cosine similarity matrix
* `Model_Training.ipynb` — Model development and preprocessing notebook

## 🎯 Project Goal

The goal of this project is to build a practical **Machine Learning recommendation system** that demonstrates how Natural Language Processing and text similarity techniques can be applied to real-world music recommendation problems.

## 🔮 Future Improvements

* Add personalized recommendations based on listening history
* Improve the recommendation model using advanced NLP techniques
* Add artist and genre-based filtering
* Improve the frontend UI
* Integrate a music streaming service when API access is available
