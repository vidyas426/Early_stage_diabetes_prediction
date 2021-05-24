# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:37:33 2021

@author: VIDYA
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()


from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("knn.pkl","rb")
log1=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"



#@app.route('/predict',methods=["Get"])
def predict_diabetes(Polydipsia,sudden_weight_loss,partial_paresis,Irritability,Polyphagia,Age,visual_blurring):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: numberS
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    input=np.array([[Polydipsia,sudden_weight_loss,partial_paresis,Irritability,Polyphagia,Age,visual_blurring]]).astype(np.float64)
    prediction=log1.predict(input)
    print(prediction)
    return prediction
    def test():
        st.info("The person has high risk of having heart disease")
        
    def test2():
        st.info("The person has low risk of having heart disease")


       



def main():
    st.title("Early stage Diabetes prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart failure prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Polydipsia = st.text_input("[Polydipsia"," ")
    sudden_weight_loss = st.text_input("sudden weight loss"," ")
    partial_paresis = st.text_input("partial paresis"," ")
    Irritability = st.text_input("Irritability"," ")
    Polyphagia = st.text_input("Polyphagia"," ")
    Age = st.text_input("Age"," ")
    visual_blurring = st.text_input("visual blurring"," ")
    
    result=""
    if st.button("Predict"):
        result= predict_diabetes(Polydipsia,sudden_weight_loss,partial_paresis,Irritability,Polyphagia,Age,visual_blurring)
        
    st.success('The output is {}'.format(result))
    
    if result == 0:
        st.text('The person has low risk of having Diabetes')
    if result ==1:
        st.text('The person has high risk of having Diabetes')
    
    
    

    
    
        
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()