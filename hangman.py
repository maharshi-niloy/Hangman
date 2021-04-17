import random
from Hangman.words_repository import words
import string


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives = 6

    while len(word_letters) != 0 and lives != 0:
        print(f'You have {lives} lives left. You have used these letters:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word is: ', ' '.join(word_list), '\n')

        user_letters = input('Guess a letter: ').upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word:
                word_letters.remove(user_letters)
            else:
                lives -= 1

        elif user_letters in used_letters:
            print('You have guessed this letter. Please try again')
        else:
            print('Invalid Character. Please try again')

    if lives == 0:
        print('Game over. You used all of your lives. The word was ', word)
    else:
        print('You have won! You guessed the word correctly.')
