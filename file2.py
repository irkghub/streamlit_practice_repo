import streamlit as st

# Title of the app
st.title("Band Name Generator Game!")

# User input for city
city = st.text_input("Which city were you born in?")

# User input for pet name
pet_name = st.text_input("Did you have a pet? What did you use to call it?")

# Button to generate the band name
if st.button("Generate Band Name"):
    if city and pet_name:
        # Generate the band name
        band_name = f"{city} {pet_name} is here folks!"
        st.success(band_name)
        st.write("When's your next show?")
    else:
        st.error("Please enter both your city and pet's name!")