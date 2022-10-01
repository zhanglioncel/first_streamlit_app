#import pandas
import streamlit

import snowflake.connector
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My Parents New Healthy Dinner")
streamlit.header("🍞Breakfast Menu")
streamlit.text("🥣Omega3 & Blueberry Oatmeal")
streamlit.text("🥗Kale,Spinach")
streamlit.text("🐔Rocket Smoothie")
streamlit.text("🥑Hard-Boiled Free-Range Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index("Fruit")

fruits_selected =streamlit.multiselect("Pick Some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show);

 #streamlit.dataframe(my_fruit_list)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_respose = fruityvice_response = requests.get("https://fruityvice.com/api/fruit"+this_fruit_choice)
   fruityvice_normalized =pandas.json_normalize(fruityvice_respose.json())
   return fruityvice_normalized 
 
#import requests

streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
 if not fruit_choice:
  streamlit.error("Please select a fruit to get information") 
 else:
   back_from_function = get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
#   fruityvice_respose = fruityvice_response = requests.get("https://fruityvice.com/api/fruit"+fruit_choice)
 #  fruityvice_normalized =pandas.json_normalize(fruityvice_respose.json())
 #  streamlit.dataframe(fruityvice_normalized)
except URLError as e: 
    streamlit.error()
 #streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

streamlit.stop()



# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
 
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list");
       return my_cur.fetchall()        

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding  ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
