import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError
import requests as req
#import snowflake.connector

streamlit.title("My Parents' New Healthy Diner") 

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
# New section to display fruityvice API Response
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
# streamlit.write('The user entered ', fruit_choice)# Calling API from Streamlit
   if not fruit_choice:
         streamlit.error("Please select a fruit to get information.")
   else:
         
         # st.text(fruityvice_response.json()) # Writes the data on screen
         # Take the JSON response and normalize it 
         # Output it on the screen as a table
         streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
    streamlit.stop()


streamlit.header("The fruit load list contains:")
# Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
# Add a button to load the data
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.dataframe(get_fruit_load_list())
    
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * FROM fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

# add_my_fruit = streamlit.text_input('Which fruit would you like to add?', 'jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)

# my_cur.execute("insert into fruit_load_list values('from streamlit')")

# Allow the User to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values("new_fruit")")
         return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('Which fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.text(insert_row_snowflake(add_my_fruit))
