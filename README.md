# Hangman Game with NLTK
This Hangman game is an enhanced version of the classic word-guessing game built using Python and Pygame. It now incorporates NLTK (Natural Language Toolkit) to provide a broader vocabulary of words to guess. Try to guess the secret word correctly before running out of chances!
## Prerequisites
Before you start playing the game, make sure you have the following:
- Python installed on your system.
- Pygame library installed. You can install it using pip:
```
pip install pygame
```
- NLTK library installed. You can install it using pip:
```
pip install nltk
```
## How to Play
1. **Running the Game:** To start the game, run the Python script provided in your local environment.
```
python main.py
```
2. **Game Rules:** You will be presented with a secret word, and you need to guess it one letter at a time. You have a limited number of chances to make incorrect guesses. The game will display underscores for each letter in the word that you need to guess.
3. **Guessing Letters:** Use the keyboard to enter a letter. If the letter is in the word, it will be revealed; otherwise, you will lose a chance. Repeated guesses of the same letter are not penalized.
4. **Winning and Losing:** You win the game by correctly guessing the entire word before running out of chances. If you run out of chances, you lose the game.
5. **Restart:** After winning or losing, press any key to restart the game.
## Game Features
- **Animated Sans:** Enjoy animated Sans characters from Undertale throughout the game.
- **Sound Effects:** The game includes various sound effects to enhance the gaming experience.
- **Interactive UI:** The game provides a colorful and interactive user interface to make your gaming session enjoyable.
- **Expanded Vocabulary:** Thanks to NLTK, the game now has access to a broader range of words, making each playthrough unique.
## Word Database
The game randomly selects words from NLTK's English word corpus. This corpus contains a vast collection of English words, making the game more challenging and diverse.
## Contributions
This project is an enhanced Hangman game built with Pygame and NLTK. Contributions to improve gameplay, add features, or enhance the user interface are welcome. Feel free to fork the project and create pull requests.
## Disclaimer
This Hangman game is meant for entertainment and educational purposes. It may not provide an extensive gaming experience but is a fun way to spend some time guessing words with an expanded vocabulary.