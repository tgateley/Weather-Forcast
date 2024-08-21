import streamlit as st
import plotly.express as px

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select how many days are forecasted")
option = st.selectbox("Select Data to View",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = []
temperatures = []
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "Y": "Temperature (C)"})
st.plotly_chart(figure)
