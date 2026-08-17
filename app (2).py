
import pickle
import streamlit as st


# =========================
# Default Music Image
# =========================

DEFAULT_IMAGE = "https://i.postimg.cc/0QNxYz4V/social.png"


# =========================
# Recommendation Function
# =========================

def recommend(song):

    index = music[music["song"] == song].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_music_names = []
    recommended_music_posters = []

    for i in distances[1:6]:

        song_name = music.iloc[i[0]].song

        recommended_music_names.append(song_name)
        recommended_music_posters.append(DEFAULT_IMAGE)

    return recommended_music_names, recommended_music_posters


# =========================
# Load Model
# =========================

music = pickle.load(
    open("df.pkl", "rb")
)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)


# =========================
# Frontend
# =========================

st.header("Music Recommender System")

music_list = music["song"].values

selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)


# =========================
# Recommendation Button
# =========================

if st.button("Show Recommendation"):

    recommended_music_names, recommended_music_posters = recommend(
        selected_song
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])

    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])

    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])

    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
