import streamlit as st
import pickle

movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

st.header("Movie Recommender System")
movie_list=movies['title'].values
selected_movie=st.selectbox("Type of select a movie from dropdown",movie_list,index=None)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movie_names=[]
    for i in distances:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

if st.button("Show Recommendations"):
    recommended_movie_names=recommend(selected_movie)
    for i in range(0,10,1):
        st.subheader(recommended_movie_names[i])
