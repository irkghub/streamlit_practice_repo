
from calendar import isleap
import streamlit as st

def check_leap(year):
    return isleap(year)
    
st.title("Leap Year Checker")
year = st.number_input("Enter the year",min_value=1)

if st.button("Check"):
    if check_leap(year):
        st.success("The year is a leap year")
    else:
        st.error("The year is not a leap year")