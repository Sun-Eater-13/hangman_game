import string
import random

wordlist = list(string.ascii_lowercase)

with open("words_hangman.py", "r", encoding="utf-8") as second_file:
    words_hangman = [line.strip() for line in second_file]

while True:
    correct_word = random.choice(words_hangman)
    if len(correct_word) >= 5:
        break

blank_word = ""
for letter in list(correct_word):
    blank_word += "_"
print(f"This is the word that You try to guess: {blank_word}\nYou have 6 guesses\n")

incorrect_letters = []
max_incorrect_guesses = 6

while max_incorrect_guesses > 0:
    guess_control = 0
    while guess_control == 0:
        guess = str(input("Guess a letter: "))
        match len(guess):
            case 1:
                if guess.lower() in wordlist:
                    guess_control += 1
                else:
                    print("Guess correctly again by choosing a letter")
            case _:
                print("Guess again by imputing exactly ONE letter")

    if guess in list(correct_word):
        print("This letter is in the word")
        count_letters = list(correct_word).count(guess)
        position_in_correct_word = 0
        for letter in range(0, len(list(correct_word))):
            if list(correct_word)[position_in_correct_word] == guess:
                blank_word = blank_word[:letter] + guess + blank_word[letter + 1:]
            position_in_correct_word += 1
    else:
        print("This letter is NOT in the word")
        incorrect_letters.append(guess)
        max_incorrect_guesses -= 1
    print(f"You can guess {max_incorrect_guesses} more times\n")
    print(f"This is the correct word: {blank_word}")
    print(f"These are incorrect letters: {', '.join(incorrect_letters)}\n")

    if blank_word == correct_word:
        break

if max_incorrect_guesses == 0:
    print(f"You lost. The correct word is {correct_word}")
else:
    print("You won")