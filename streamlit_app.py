import streamlit as st
import pandas as pd

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
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Banana'])

# Display the table on the page
st.dataframe(my_fruit_list)