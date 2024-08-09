import joblib
import streamlit as st
clf_knn=joblib.load("clf_knn_model")
st.title("Weight Height Classifier")
wt=st.slider("Enter the weight of the person(in kg)",min_value=40,max_value=100,value=55,step=1)
ht=st.slider("Enter the height of the person(in cm)",min_value=135,max_value=190,value=165,step=1)

if (st.button("PREDICT CLASS")):
    op=clf_knn.predict([[wt,ht]])
    st.subheader(f'The person having weight as {wt}kg and height as {ht}cm is categorized as {op[0]}.')
