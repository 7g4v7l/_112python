import streamlit as st
import datetime

title = st.text_input('Movie title','aa')
st.write('The current movie title is', title)


number = st.number_input('Insert a number',10)
st.write('The current number is ', number)


d = st.date_input(
    "When\'s your birthday",
    datetime.date(2000, 7, 6))
st.write('Your birthday is:', d)