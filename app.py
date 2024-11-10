import streamlit as st
import random

#Page name and icon
st.set_page_config(page_title="Animal Guessing Game", page_icon=":paw_prints:")

#Introduction to the game
st.write("""
    Welcome to the Animal Guessing Game!\n
    Please guess the animal I am thinking about. The options are:\n
    fly, spider, mouse, rat, bird, rabbit, monkey, cat, racoon,\n
    fox, pig, panda, dog, wolf, lion, horse, giraffe, elephant, whale🐾""")

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

#Function for qualitative feedback
def feedback_score(guess_animal, target_animal):
    score = 0

#Defining variables to calculate quality of guess
    guess_features = animals[guess_animal]
    target_features = animals[target_animal]
    total_features = len(target_features)

#Calculate the amount of same features
    for feature in target_features:
        if guess_features[feature] == target_features[feature]:
            score += 1

#Return the similarity value
    return score/total_features

#Function to show animal picture
def show_animal(animal_name):
    try:
        image_path = f"images/{animal_name}.jpg"
        st.image(image_path, caption=animal_name, use_container_width=True)
    except:
        st.warning(f"Didn't find the image for '{animal_name}'")

#Function to see if the input is valid and correct
def check_input(guess_animal, target_animal):
    if guess_animal not in animals:
        st.write("This animal is not available to be guessed...")
    else:
        if guess_animal == target_animal:
            st.write("Wow! You found the right animal! Congrats!")
            show_animal(target_animal)
        else:
            give_feedback(guess_animal, target_animal)

#Function to give qualitative feedback based on feedback score
def give_feedback(guess_animal, target_animal):
    score = feedback_score(guess_animal, target_animal)
    if score == 0:
        st.write("I'm sorry. The animal you are looking has almost no similarities to your guess...😥")
    elif score <= 0.2:
        st.write("You are getting there. But there is still a looong way to go... Good luck!!🧸")
    elif score <= 0.4:
        st.write("Well... The animal you are looking for has a few similarities to your guessed animal😅")
    elif score <= 0.6:
        st.write("Not quite the animal you are looking for but you are guessing in the right direction. The animals are quite similar😺")
    elif score <= 0.8:
        st.write("The animal you guessed is very similar to the animal you are looking for😍")
    elif score == 1:
        st.write("Wow the animal you guessed is almost the same animal!😻")

#Create attempts counter for stats
attempts = 0

#Initialize session state
if 'animal' not in st.session_state:
    animal, animal_features = random.choice(list(animals.items()))
    st.session_state.animal = animal
    st.session_state.animal_features = animal_features
    st.session_state.attempts = attempts
    st.session_state.game_over = False

#Just for testing
#st.write(st.session_state.animal)

#Ask for a guess
guess = st.text_input("What is your guess:", "")

#Create Guess Button and check the Input
if st.button("Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1
    check_input(guess, st.session_state.animal)