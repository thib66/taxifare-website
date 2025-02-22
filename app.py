import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel frontal
'''

url = 'https://taxifare.lewagon.ai/predict'


date_taxi = str(st.date_input("Date"))
time_taxi = str(st.time_input("Time"))
pickup_longitude= str(st.text_input('Pick-up longitude', '-73.950655'))
pickup_latitude= str(st.text_input('Pick-up latitude', '40.783282'))
drop_off_longitude= str(st.text_input('Drop-off longitude', '-73.984365'))
drop_off_latitude= str(st.text_input('Drop-off latitude', '40.769802'))
nb_of_passengers = str(st.slider('Passenger count', 1, 5, 3))
st.write(date_taxi)
st.write(time_taxi)
def get_map_data():

    return pd.DataFrame(
            [[float(pickup_latitude), float(pickup_longitude)],
            [float(drop_off_latitude), float(drop_off_longitude)]],
            columns=['lat', 'lon']
        )

requete=url+"?pickup_datetime="+date_taxi+"+"+time_taxi+\
                 "&pickup_longitude="+pickup_longitude+\
                 "&pickup_latitude="+pickup_latitude+\
                 "&dropoff_longitude="+drop_off_longitude+\
                 "&dropoff_latitude="+drop_off_latitude+\
                 "&passenger_count="+nb_of_passengers
if st.button('Prédiction  /Estimation'):
    r = requests.get(requete).json()
    st.write("The fare is "+str(round(r['fare'],2))+" USD")
    df = get_map_data()
    st.map(df)

else:
    st.write('En attente de renseignements 😞')

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()