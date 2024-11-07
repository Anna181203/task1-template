import streamlit as st
import random

#Page name and icon
st.set_page_config(page_title="Animal Guessing Game", page_icon=":paw_prints:")

#Introduction to the game
st.write("Welcome to the Animal Guessing Game!")
st.write("Please guess the animal I am thinking about. The options are:")
st.write("fly, spider, mouse, rat, bird, rabbit, monkey, cat, racoon,")
st.write ("fox, pig, panda, dog, wolf, lion, horse, giraffe, elephant, whale")