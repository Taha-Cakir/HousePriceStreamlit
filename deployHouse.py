import streamlit as st
from PIL import Image
from DidemTaha.eda.eda import *
# import pickle
import joblib
import webbrowser


pickle_in = open('HPrice.pkl', 'rb')
regressor = joblib.load(pickle_in)

st.title("House Price Prediction")

# st.set_page_config(layout='wide', page_title="Predict price of House that you always wanted to ! ",
#                    page_icon="🏠")

title = '<h1 style="Arial, sans-serif; color:#323000; font-size: 53px;text-align: center">Calculate your dream Houses Price that you always wanted to! 🏠 </h1>'
st.markdown(title, unsafe_allow_html=True)

select = st.sidebar.selectbox('House Price', ['Predict The Prices'], key='1')


# select = st.sidebar.selectbox('Select Action', ['Check the visualizations'], key='2')

if not st.sidebar.checkbox("Hide", False, key='1'):
    st.title(' Calculation')
    name = st.text_input("Name: ")
    msquare = st.number_input("Total Square : ", min_value=1, max_value=100000, value=10, step=1)
    buildingAge = st.number_input("Building Age : ", min_value=1, max_value=100000, value=10, step=1)
    lotQual = st.number_input("Lot Quality: ", min_value=1, max_value=10000000, value=10, step=1)
    GarageArea = st.number_input("Garage Area : ", min_value=1, max_value=10000000, value=10, step=1)
    GrLivArea = st.number_input("Living Area(Except Basement) : ", min_value=1, max_value=10000000, value=10, step=1)
    overallQual = st.number_input("Overall Quality: ", step=1,value=10)
    totalQual = st.number_input("Total Quality: ",value=overallQual*GrLivArea*GarageArea)
    budget = st.number_input("Budget :  ")



    if st.button('Predict'):
        a = regressor.predict([[msquare, buildingAge, totalQual, lotQual]])
        if a > budget :
            st.warning(f"You exceed the budget approximately {a - budget} House Price is {a}")

            # st.warning("You exceed the budget approximately ", {a - budget})
        else:
            st.success(f"House price is {a} you will {budget - a} save ")



        # st.metric(label="House price : ", value=a)
        """
-------------------------------------------------------------------------------
"""
st.markdown(" ### Check out our LinkedIn accounts !")

url = 'https://www.linkedin.com/in/didem-erkan/'

if st.button('Didem Erkan  ➡'):
    webbrowser.open_new_tab(url)

url1 = 'https://www.linkedin.com/in/belguzardamat/'

if st.button('Belgüzar Damat ➡'):
    webbrowser.open_new_tab(url1)

url2 = 'https://www.linkedin.com/in/gamzeakman/'

if st.button('Gamze Akman  ➡ '):
    webbrowser.open_new_tab(url2)


url4 = 'https://www.linkedin.com/in/burakuzn/'

if st.button('Burak Uzun  ➡'):
    webbrowser.open_new_tab(url4)

url5 = 'https://www.linkedin.com/in/cansinkutlucan/'

if st.button('Cansın Kutlucan  ➡'):
    webbrowser.open_new_tab(url5)

url6 = 'https://www.linkedin.com/in/danabasozan/'

if st.button('Ozan Danabas  ➡'):
    webbrowser.open_new_tab(url6)

url7 = 'https://www.linkedin.com/in/taha-cakir/'

if st.button('Taha Çakır  ➡'):
    webbrowser.open_new_tab(url7)

from bokeh.models.widgets import Div










