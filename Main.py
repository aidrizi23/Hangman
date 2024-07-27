import random
import os

from english_words import get_english_words_set
from stages import stages

web2lowerset = get_english_words_set(['web2'], lower=True)
word_list = list(web2lowerset)
chosen_word = random.choice(word_list)
lives = 6
guessed_until_now = ""
display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False

def clear_console():
    # Use ANSI escape sequence to clear the console
    print("\033c", end="")

while not end_of_game:
    clear_console()
    guess = input("Please enter a character: ").lower()
    while len(guess) > 1 and guess.isalpha():
        guess = input("Please enter a valid letter")
    while guess in guessed_until_now:
        guess = input("You have already chosen this letter, please select another one")
    guessed_until_now += guess
    if guess in chosen_word:
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    else:
        lives -= 1
    print(f"{lives} lives leftz")
    print(display)
    print(stages[lives])
    if '_' not in display:  # means that all the letters have been found
        end_of_game = True
        print("You Win")
    if lives == 0:
        end_of_game = True
        print("LOST NIGGA")
        print(f"The word was {chosen_word}")
  