import streamlit as st
import pandas as pd

# Statistics calculation
games_played = st.session_state.get("games_played", 0)
total_guesses = st.session_state.get("total_guesses", 0)
average_guesses = total_guesses / games_played if games_played > 0 else 0
guess_counts = st.session_state.get("guesses_per_game", [])

st.title("📊 Game Statistics")

# Display statistics
st.write(f"**Total Games Played**: {games_played}")
st.write(f"**Average Guesses per Game**: {average_guesses:.2f}")

# Bar chart for guesses per game
if guess_counts:
    # Create a DataFrame with the guess counts
    df = pd.DataFrame({
        "Game": [f"Game {i+1}" for i in range(len(guess_counts))],
        "Guesses": guess_counts
    })
    st.write("### Guesses per Game")
    st.bar_chart(df.set_index("Game"))
else:
    st.write("No data available for guesses per game.")

st.subheader("Chat History")
for guess, feedback in st.session_state.guess_history:
    st.write(f"**You guessed**: {guess} - **Feedback**: {feedback}")