
import random
import streamlit as st

#Page name and icon
st.set_page_config(page_title="Animal Guessing Game", page_icon=":paw_prints:")

st.title("🐾Welcome to the Animal Guessing Game!🐾")
#Introduction to the game
st.write("""
    Please guess the animal I am thinking about. The options are:\n
    Fly, Spider, Mouse, Rat, Bird, Rabbit, Monkey, Cat, Racoon, Fox, Pig, Panda, Dog, Wolf, Lion, Horse, Giraffe, Elephant, Whale🐾""")

#List of all possible Animals
animals = {
    "fly": {"Habitat":"Everywhere", "Size":"XS", "Food":"Omnivore", "Movement":"Flying", "Color":"Black", "Reproduction:":"Oviparous"},
    "spider": {"Habitat":"Everywhere", "Size":"XS", "Food":"Carnivore", "Movement":"Walking", "Color":"Black", "Reproduction:":"Oviparous"},
    "mouse": {"Habitat":"Everywhere", "Size":"XS", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "rat": {"Habitat":"Everywhere", "Size":"S", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "bird": {"Habitat":"Everywhere", "Size":"S", "Food":"Omnivore", "Movement":"Flying", "Color":"Colorful", "Reproduction:":"Oviparous"},
    "rabbit": {"Habitat":"Everywhere", "Size":"S", "Food":"Herbivore", "Movement":"Hopping", "Color":"Brown", "Reproduction:":"Mammal"},
    "monkey": {"Habitat":"Africa", "Size":"M", "Food":"Omnivore", "Movement":"Climbing", "Color":"Brown", "Reproduction:":"Mammal"},
    "cat": {"Habitat":"Everywhere", "Size":"M", "Food":"Carnivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "racoon": {"Habitat":"America", "Size":"M", "Food":"Omnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "fox": {"Habitat":"Everywhere", "Size":"M", "Food":"Omnivore", "Movement":"Walking", "Color":"Red", "Reproduction:":"Mammal"},
    "pig": {"Habitat":"Everywhere", "Size":"L", "Food":"Omnivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "panda": {"Habitat":"Asia", "Size":"L", "Food":"Herbivore", "Movement":"Climbing", "Color":"White", "Reproduction:":"Mammal"},
    "dog": {"Habitat":"Everywhere", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "wolf": {"Habitat":"Europe", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "lion": {"Habitat":"Africa", "Size":"L", "Food":"Carnivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "horse": {"Habitat":"America", "Size":"L", "Food":"Herbivore", "Movement":"Walking", "Color":"Multi", "Reproduction:":"Mammal"},
    "giraffe": {"Habitat":"Africa", "Size":"XL", "Food":"Herbivore", "Movement":"Walking", "Color":"Brown", "Reproduction:":"Mammal"},
    "elephant": {"Habitat":"Africa", "Size":"XL", "Food":"Herbivore", "Movement":"Walking", "Color":"Grey", "Reproduction:":"Mammal"},
    "whale": {"Habitat":"Ocean", "Size":"XL", "Food":"Carnivore", "Movement":"Swimming", "Color":"Grey", "Reproduction:":"Mammal"}
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

#Function to give qualitative feedback based on feedback score
def give_feedback(guess_animal, target_animal):
    score = feedback_score(guess_animal, target_animal)
    if score == 0:
        return "I'm sorry. The animal you are looking has almost no similarities to your guess...😥"
    elif score <= 0.2:
        return "You are getting there. But there is still a looong way to go... Good luck!!🧸"
    elif score <= 0.4:
        return "Well... The animal you are looking for has a few similarities to your guessed animal😅"
    elif score <= 0.6:
        return "Not quite the animal you are looking for but you are guessing in the right direction. The animals are quite similar😺"
    elif score <= 0.8:
        return "The animal you guessed is very similar to the animal you are looking for😍"
    elif score == 1:
        return "Wow the animal you guessed is almost the same animal!😻"

#Function to see if the input is valid and correct
def check_input(guess_animal, target_animal):
    if guess_animal not in animals: #or guess_animal not in [animal.lower() for animal in animals]:
        feedback = "This animal is not available to be guessed..."
        st.write(feedback)
    elif guess_animal == target_animal:
        feedback = "Wow! You found the right animal! Congrats!"
        st.write(feedback)
        show_animal(target_animal)
        st.session_state.games_played += 1
        st.session_state.total_guesses += st.session_state.guess_count
        st.session_state.guesses_per_game.append(st.session_state.guess_count)
        st.session_state.game = True
    else:
        feedback = give_feedback(guess_animal, target_animal)
        st.write(feedback)
    st.session_state.guess_history.append((guess_animal, feedback))


#HERE THE ACTUAL GAME STARTS

#Initialize session state
if 'animal' not in st.session_state:
    animal, animal_features = random.choice(list(animals.items()))
    st.session_state.animal = animal
    st.session_state.animal_features = animal_features
    st.session_state.guess_history = []
    st.session_state.guess_count = 0
    st.session_state.games_played = 0
    st.session_state.total_guesses = 0
    st.session_state.guesses_per_game = []
    st.session_state.game = False

#Ask for a guess
guess = st.text_input("What is your guess:", "")
guess = guess.lower()

#Create Guess Button and check the Input
if st.button("Guess"):
    st.session_state.guess_count += 1
    check_input(guess, st.session_state.animal)

if st.button("Start new game") or st.session_state.game:
    animal, animal_features = random.choice(list(animals.items()))
    st.session_state.animal = animal
    st.session_state.animal_features = animal_features
    st. session_state.guess_count = 0
    st.session_state.game = False

st.write(st.session_state.animal)


