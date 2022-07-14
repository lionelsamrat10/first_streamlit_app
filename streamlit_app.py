import streamlit as st
import pandas as pd
#import snowflake.connector
st.title("My Parents' New Healthy Diner") 

st.header("Breakfast Menu")
st.text("🥣 Omega 3 and Blueberry Oatmeal")
st.text("🥗 Kale, Spinach & Rocket Smoothie")
st.text("🐔 Hard-Boiled Free-Range Egg")
st.text("🥑🍞 Avocado Toast")
 
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
st.dataframe(fruits_to_show)

# New section to display fruityvice API Response
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)# Calling API from Streamlit
import requests as req
fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json()) # Writes the data on screen

# Take the JSON response and normalize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Output it on the screen as a table
st.dataframe(fruityvice_normalized)

