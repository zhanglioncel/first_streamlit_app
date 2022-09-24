import pandas
import streamlit
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


 streamlit.dataframe(fruits_to_show)
streamlit.dataframe(my_fruit_list)
 
