import streamlit as st
import random

#Page name and icon
st.set_page_config(page_title="Animal Guessing Game", page_icon=":paw_prints:")

#Introduction to the game
st.write("""
    Welcome to the Animal Guessing Game!\n
    Please guess the animal I am thinking about. The options are:\n
    fly, spider, mouse, rat, bird, rabbit, monkey, cat, racoon,\n
    fox, pig, panda, dog, wolf, lion, horse, giraffe, elephant, whale
    🐾""")

#List of all possible Animals
animals = {
    "Fly": {"Habitat":"Everywhere", "Size":"XS", "Food":"Omnivore", "Movement":"Flying", "Color":"Black", "Reproduction:":"Oviparous"},
    "Spider": {"Habitat":"Everywhere", "Size":"XS", "Food":"Carnivore", "Movement":"Walking", "Color":"Black", "Reproduction:":"Oviparous"},
    "Mouse": {"Habitat":"Everywhere", "Size":"XS", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "Rat": {"Habitat":"Everywhere", "Size":"S", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "Bird": {"Habitat":"Everywhere", "Size":"S", "Food":"Omnivore", "Movement":"Flying", "Color":"Colorful", "Reproduction:":"Oviparous"},
    "Rabbit": {"Habitat":"Everywhere", "Size":"S", "Food":"Herbivore", "Movement":"Hopping", "Color":"Brown", "Reproduction:":"Mammal"},
    "Monkey": {"Habitat":"Africa", "Size":"M", "Food":"Omnivore", "Movement":"Climbing", "Color":"Brown", "Reproduction:":"Mammal"},
    "Cat": {"Habitat":"Everywhere", "Size":"M", "Food":"Carnivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "Racoon": {"Habitat":"America", "Size":"M", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "Fox": {"Habitat":"Everywhere", "Size":"M", "Food":"Omnivore", "Movement":"Walking", "Color":"Red", "Reproduction:":"Mammal"},
    "Pig": {"Habitat":"Everywhere", "Size":"L", "Food":"Omnivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "Panda": {"Habitat":"Asia", "Size":"L", "Food":"Herbivore", "Movement":"Climbing", "Color":"White", "Reproduction:":"Mammal"},
    "Dog": {"Habitat":"Everywhere", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "Wolf": {"Habitat":"Europe", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "Lion": {"Habitat":"Africa", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "Horse": {"Habitat":"America", "Size":"L", "Food":"Herbivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "Giraffe": {"Habitat":"Africa", "Size":"XL", "Food":"Herbivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "Elephant": {"Habitat":"Africa", "Size":"XL", "Food":"Herbivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "Whale": {"Habitat":"Ocean", "Size":"XL", "Food":"Carnivore", "Movement":"Swimming", "Color":"Grey", "Reproduction:":"Mammal"}
}