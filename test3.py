import random
import time
domestic_animals = ["cat", "goat", "cow", "sheep", "dog", "rat", "horse", "chicken"]
wild_animals = ["zebra", "lion", "leopard", "snake", "crocodile", "hyena"]
playgame = True
category = ""
guesses = []
guess_list = []
continue_game = "Y"
name = input("Enter your name: ")
time.sleep(1)
print("welcome!!!!", name.capitalize(), "to the hangman game!!yeeeeea !!!1 ")
time.sleep(1)
print("first you have to pick a category you want to guess from")
time.sleep(1)
print(r" 'd' for domestic_animals and 'w' for wild_animals 'x' for quit")
time.sleep(1)
print("you have to guess one letter at a time and you will have limited number of times")

while True:
    if category.lower() == "d":
        secret_word = random.choice(domestic_animals)
        break
    elif category.lower() == "w":
        secret_word = random.choice(wild_animals)
        break
    else:
        category = input("category you have entered:")
    if category.lower() == "x":
        print("bye")
        playgame = False
        break
    if playgame:
        secret_list = list(secret_word)
        attempts = (len(secret_word) + 2)
        