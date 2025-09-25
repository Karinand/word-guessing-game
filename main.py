import random
import json

filename = 'words_dictionary.json'

try:
    with open(filename) as words_file:
        data = json.load(words_file)
except FileNotFoundError:
    print('Error: The json file words dictionary not found')
except json.JSONDecodeError:
    print('Error: Failed to parsing the JSON data')
except Exception as e:
    print(f'Error: {e}')

# Randomly choose a word from dictionary
word_to_guess = random.choice(list(data.keys()))
attempt = 10

total_word = len(word_to_guess)
guessed_word = ['_'] * total_word

print('Welcome to the Word Guessing Game!')
print(' ' . join(guessed_word) + ' (' + str(total_word) + '-letter word)')

while attempt > 0 and '_' in guessed_word:
    print('\nCurrent word: ' + ' ' . join(guessed_word))
    guess = input('Guess a letter: ').lower().strip()

    # Validate the guess letter
    if not guess:
        print("Please enter a letter.")
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Validate the letter to the guess word
    if guess in word_to_guess:
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[idx] = guess
        print("Great guess!")
    else:
        attempt -= 1
        print('Wrong guess! Attempts left: ' + str(attempt))
    
    if '_' not in guessed_word:
        print('\nCongratulations!! You\'ve guessed the word: ' + word_to_guess)
        break
else:

    print(f"\nGame over! The word was: {word_to_guess}")
