# Hangman Game with NLTK and Language Selection
![alt text](/assets/mainGame.png)
Introducing the Hangman game with enhanced features and language selection. This game is built using Python and Pygame and incorporates NLTK for a broader vocabulary. This version of the game is designed for easy setup using a `requirements.txt` file, making installation a breeze. You can enjoy playing the game with a wider vocabulary and language customization.  Let's get started!
## Prerequisites
Before you start playing the game, make sure you have the following:
- **Python:** Make sure Python is installed on your computer. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Virtual Environment (Optional)**: It's recommended to use a virtual environment to manage dependencies and avoid conflicts with your system-wide Python packages. You can create a virtual environment using the following commands:
```
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS and Linux
python -m venv myenv
source myenv/bin/activate
```
- Requirements File: This version of the game comes with a requirements.txt file that specifies all the required dependencies. To install these dependencies, run the following command:
```
pip install -r requirements.txt
```
This will install `Pygame`, `NLTK`, `Google Translate API`, and `Unidecode` automatically.
## How to Play
1. **Running the Game:** To start the game, run the Python script provided in your local environment.
```
python main.py
```
2. **Language Selection:** At the beginning of the game, you can choose your preferred language by using the UP and DOWN arrow keys and pressing ENTER.
3. **Game Rules:** You will be presented with a secret word, and you need to guess it one letter at a time. You have a limited number of chances to make incorrect guesses. The game will display underscores for each letter in the word that you need to guess.
4. **Guessing Letters:** Use the keyboard to enter a letter. If the letter is in the word, it will be revealed; otherwise, you will lose a chance. Repeated guesses of the same letter are not penalized.
5. **Winning and Losing:** You win the game by correctly guessing the entire word before running out of chances. If you run out of chances, you lose the game.
6. **Restart:** After winning or losing, press any key to restart the game. You can also press ESCAPE to return to the language selection menu.
## Game Features
- **Animated Sans:** Enjoy animated Sans characters from Undertale throughout the game.
- **Sound Effects:** The game includes various sound effects to enhance the gaming experience.
- **Interactive UI:** The game provides a colorful and interactive user interface to make your gaming session enjoyable.
- **Expanded Vocabulary:** Thanks to NLTK, the game now has access to a broader range of words, making each playthrough unique.
- **Language Selection:** Choose your preferred language to play the game. The game supports multiple languages.
- **Translation:** The game can translate messages into your selected language for a fully immersive experience.
## Word Database
The game randomly selects words from NLTK's English word corpus. This corpus contains a vast collection of English words, making the game more challenging and diverse.
## Language Selection
You can choose your preferred language from a list of available languages at the beginning of the game. This feature provides a fully localized experience.
## Contributions
This project is an enhanced Hangman game with language selection built with Pygame, NLTK, and the Google Translate API. Contributions to improve gameplay, add features, or enhance the user interface are welcome. Feel free to fork the project and create pull requests.
## Disclaimer
This Hangman game is meant for entertainment and educational purposes. It may not provide an extensive gaming experience but is a fun way to spend some time guessing words with an expanded vocabulary and language selection. Enjoy the game!