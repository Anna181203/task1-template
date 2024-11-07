STEP BY STEP GUIDE FOR TASK 1
=============================

Part 1: Create and test your development environment

1. Make sure the content of this archive is extracted in a separate directory.
2. Create a Python Virtual Environment in this directory (see Courseware)
3. Activate the environment
4. Install the requirements: pip install -r requirements.txt
5. Try to run the demo app: streamlit run app.py

Part 2: Create github repository and test deployment

1. Modify the demo.py app at your convenience (see https://docs.streamlit.io/develop/api-reference/text for text formatting options, also look at the Media and Layout sections)
2. Create a github account (if you don't have one yet) and create an empty repository. Look for the repository https URL.
3. Make your local folder a git repository and connect it to the github repository (see Courseware)
4. Commit and push your code
5. Create an accout at streamlit.io and click on "Create app". Connect to your github account by following the instructions. Select app.py as the script to run and deploy your app.
6. Voila! Streamlit should display a URL that you can use to access your app on the streamlit community server. This is not limited to you but everyone who knows this URL can. (So be careful what you include in your app)

Part 3: Start working on the task

1. Think of a guessing game that you like to implement.
2. Modify the app.py file (or create a new one):
-- At first, don't care about the guessing logic. Create a nice interface.
-- Make sure you have an input widget for the guesses and check the results against a fixed value. Implement the feedback logic.
-- Now take care of the real guessing logic: a) Initialize a new goal if neccessary, b) Check if guess meets the goal, c) Provide feedback
3. Create and update data structures for statistics and chat view (counting guesses, perhaps maintaining a history etc.)
4. Transform your guessing and feedback interface to a chat interface (see https://docs.streamlit.io/develop/api-reference/chat ). Look at https://streamlit.io/generative-ai for a chat example (the OpenAI connection will only be made in part 2 of the task, just look at the overall structure and the data structures)
5. Make your app a multipage app by creating a new file for the navigation (see https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation) and a dummy file for the statistics
6. Add logic to the statistics file
7. Test everything and, if happy, commit, push and deploy!

Part 1 of task 1 is already done with this!

Here's the full task (see Vips for potentialls updated versions):


TASK 1
======

Objectives
----------

Create a streamlit app that fulfills the following requirements.

Basic requirements (max. 70% of points):

The app has at least two pages: "Play" and "Stats"

"Play" page:

- The "Play" page features a guessing game in which the user guesses something and the app evaluates guesses, giving hints and checking whether the guessing goal was found.
- The guessing game uses Streamlit's chat component.

"Stats" page:

- The "Stats" page displays some stats about playing like the number of games played, the average number of guesses per game. 
- The "Stats" page displays a bar chart showing he number of guesses for each game
Stability and Usability:

- The app works and does not crash, even for malformed input
- The app has a clean, logical look and is intuitive to be use

Code quality:

- The code is making use of streamlit features in a good way
- The code is not longer and more complex than necessary
- The code includes comments

Additional requirements  I (max. 15% of points):
------------------------------------------------

Implement the following improvements:

The guessing game involves natural language processed by a LLM (Open AI key is provided), e.g. an animal guessing game with yes/no answers
The game is interesting to play and the evaluation works correct for he vast majority of cases

Additional requirements II (max. 15 of points):
-----------------------------------------------

Implement the following improvements:

The app is able to estimate the quality of guesses
The estimated guessing qualiy if presented on the stats page in an interesting and transparent way to the user

