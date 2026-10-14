# Joke API CLI

A simple command-line joke generator built in Python. Fetches jokes in real time from [JokeAPI](https://v2.jokeapi.dev/) based on the category you choose.

## Features
- Get a random joke
- Get a joke from a specific category (Programming, Pun, Spooky)
- Handles both single-line and setup/punchline joke formats
- Graceful error handling for failed API requests or invalid input

## Tech Used
- Python
- `requests` library for API calls

## How to Run
1. Install the requests library: `pip install requests`
2. Run the script: `python joke.py`
3. Pick an option from the menu (1-5)

## What I Learned
Working with this project helped me understand how to make real HTTP requests, parse JSON responses into Python dictionaries, and handle different response shapes returned by an external API.
