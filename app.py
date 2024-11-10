import streamlit as st
import random

#Page name and icon
st.set_page_config(page_title="Animal Guessing Game", page_icon=":paw_prints:")

#Introduction to the game
st.write("Welcome to the Animal Guessing Game!")
st.write("Please guess the animal I am thinking about. The options are:")
st.write("fly, spider, mouse, rat, bird, rabbit, monkey, cat, racoon,")
st.write ("fox, pig, panda, dog, wolf, lion, horse, giraffe, elephant, whale, test")

animals = {
    "Fly": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Spider": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Mouse": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Rat": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Bird": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Rabbit": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Monkey": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Cat": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Racoon": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Fox": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Pig": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Panda": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Dog": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Wolf": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Lion": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Horse": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Giraffe": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Elephant": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""},
    "Whale": {"Habitat":"", "Size":"", "Food":"", "Movement":"", "Color":"", "Reproduction:":""}
}