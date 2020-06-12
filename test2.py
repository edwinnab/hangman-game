#we use the time and random modules
#from the random module use choice() method to pick words from our word list
#from time module use sleep() method to introduce delays
import random
import time
#create word lists
#program will randomly pick a word from the category you select
programming_languages = ["python", "java", "c++", "c#", "visual basic", "ruby on rails", "r programming", "assembly", "julia"]
programming_units = ["calculus", "operting system", "software engineering", "machine learning", "data science", "deep learning"]
#variables for user
playgame = True
category = ""
guesses = []
guess_list = []
continue_game ="Y"
#game info welcome and introduce the user to the game
user_name = input("Enter your name: ")
print("welcome! ", user_name.upper(), "lets play hangman!!!!!")
time.sleep(1)
print(r"first you have to pick a category either 'u' for programming_units or 'l' for programming languages.")
print("You are supposed to guess the word that the computer will randomly select.")
time.sleep(1)
print("Guess one letter at a time, and you will have a limit to the number of times you can guess a letter.")
time.sleep(1)
print("Have lots of fun!!!!!")
time.sleep(1)
print(r"type 'x' to quit")
#logic for the program to choose
# random word from the categories
while True:
    if category.lower() == "l":
        secret_word = random.choice(programming_languages)
        break
    elif category.lower() == "u":
        secret_word = random.choice(programming_units)
        break
    else:
        category = input(r"You have to use either 'l' or 'u' to pick a category and 'x' to quit.")
    if category.lower() == "x":
        print("Bye!!! see you next time")
        playgame = False
        break
    #converts our secret word to a list 
    if playgame:
        secret_word_list = list(secret_word)
    #shows the number of attempts 
        attempts = (len(secret_word) + 2)
        def printGuessedLetters():
            print("your secret word is: "  + "".join(guess_list))
        for n in secret_word_list:
            guess_list.append("_")
        printGuessedLetters()
        print("The number of allowed attempts is:", attempts)


