import streamlit as st
import pandas as pd

# Statistics calculation
games_played = st.session_state.get("games_played", 0)
total_guesses = st.session_state.get("total_guesses", 0)
average_guesses = total_guesses / games_played if games_played > 0 else 0
guess_counts = [len(game[1]) for game in st.session_state.get("guess_history", [])]