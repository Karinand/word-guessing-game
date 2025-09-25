# Word Guessing Game with Python

This is a **Word Guessing Game** implemented in Python. The game is based on a tutorial from **[Codedex](https://www.codedex.io/projects/build-a-word-guessing-game-with-python)**, with modifications made to integrate a larger and more diverse list of english words from the Github repository **[dwyl/english-words](https://github.com/dwyl/english-words)**

### Features
- Play a classic word-guessing game in the terminal.
- The game picks a random word from a list of valid English words.
- You have a limited number of guesses (10) to guess the word correctly
- After each guess, the game provides feedback on how many letters amtch.

### Setup and Requirements
To play the game, you need to have **Python** installed on your computer

1. **Clone the repository**:
    First clone the repository to your local machine by running the following command in your terminal:
    ```
    git clone https://github.com/Karinand/word-guessing-game.git
    cd word-guessing-game
    ```

2. **Download the Word List**:
   The game uses a list of English words from the GitHub repository [dwyl/english-words](https://github.com/dwyl/english-words). You can either download the file manually from the provided link, or use the provided file in this repository.

### How to Play:
1. **Run the Game**:
   After setting up the project and downloading the word list, you can start the game by running the following command:
   ```bash
   python main.py
   ```

2. **Guessing the Word**:
   - The game will pick a random word from the list.
   - You have to guess the word letter by letter.
   - The game will provide feedback after each guess, indicating how many letters are correct and in the right position.
   - You have a limited number (10) of guesses to guess the word.

3. **Example Gameplay**:
   ```bash
   Welcome to the Word Guessing Game!
   _ _ _ _ _  (5-letter word)

   Guess a letter: e
   Correct letters: _ _ e _ _

   Guess a letter: t
   Correct letters: t _ e _ _
   ```

### Game Logic:
- The game picks a random word from a list of words contained in **`words_dictionary.json`**.
- The word is hidden from the player, and the player must guess the letters one by one.
- The game will tell the player how many letters they guessed correctly and give them a limited number of attempts to guess the full word.

### Game Files:
- **`main.py`**: The main Python script that runs the word guessing game.
- **`words_dictionary.json`**: The file containing the list of valid words for the game.

### Troubleshooting:
- **Missing File**: If the `words_dictionary.json` file is missing, the game will print an error and exit.
- **Invalid Guesses**: The game currently accepts single-letter guesses and ignores invalid inputs (e.g., multiple letters, numbers, or special characters).
