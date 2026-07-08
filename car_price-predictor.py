import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st


def main():
    html_temp = """<h1>Car Price Prediction</h1>"""

    model = xgb.XGBRegressor()
    model.load_model("car_prediction_XGB model.json")

    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("This app will help you to predict your car selling price")

    p1 = st.number_input("Please enter ex-showroom price(IN Lakhs)",2.5,25.0,step=1.0)
    p2 = st.number_input("Please enter car driven(IN Kilometers)",100,500000,step=100)
    s1 = st.selectbox("select the fuel type",("Petrol","Diesel","CNG"))         
    if s1 =='Petrol':
        p3 = 0
    elif s1 == 'Diesel':
        p3=1
    elif s1=='CNG':
        p3=3   

    s2 = st.selectbox("Select the seller_type",("Dealer","Individual"))
    if s2=="Dealer":
        p4=0
    elif s2=="Individual":
        p4=1    
    s3 = st.selectbox("Select the Transmission",("Manual","Automatic"))
    if s3=="Manual":
        p5=0
    elif s3=="Automatic":
        p5=1   

    p6 = st.slider("How many Owners",0,3)

    date_time = datetime.datetime.now()
    years = st.number_input("Car Purchased year",1990,date_time.year,step=1)   
    p7 = date_time.year - years    

    data_new = pd.DataFrame({
    'Present_Price':5.59,
    'Kms_Driven':27000,
    'Fuel_Type':0,
    'Seller_Type':0,
    'Transmission':0,
    'Owner':2,
    'Age':12
},index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        st.success("You can sell your car {:.2f} lakhs ".format(pred[0]))

if __name__=='__main__':
    main()