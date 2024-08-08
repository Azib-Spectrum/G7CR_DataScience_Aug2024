import streamlit as st
import joblib
final_model=joblib.load(r"C:\Users\Ameer\Downloads\G7 CR DataScience\lr_model")
st.title("Salary predictor based on Years of Experience")
st.text("This app is created by using Streamlit")
st.text("This is powered by using Linear Regression module of sklearn library")
st.subheader("Please enter the number of years of experience and click on PREDICT")
yrs=st.number_input("Years of Experience",min_value=0.0,max_value=15.0,value=3.0,step=0.5)
if(st.button("PREDICT SALARY")):
    op=final_model.predict([[yrs]])
    st.header(f"The estimated salary for a person having {yrs} years of experience is ₹{round(op[0])}.")
