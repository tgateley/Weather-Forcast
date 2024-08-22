import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select how many days are forecasted")
option = st.selectbox("Select Data to View",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    data, date = get_data(place, days)

    if option == "Temperature":
        data = [dict["main"]["temp"] for dict in data]
        figure = px.line(x=date, y=data, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
