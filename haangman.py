#import the time module
import time
name = input(r"What's your name: ")
print("welcome ", name, "time to play hangman!")
#wait for a second
time.sleep(1)
print(name, "start guessing......")
word = "secret"
guesses = ""
#determine the number of turns
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won")
        break
    guess = input("guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("You have", + turns, "more guesses")
        if turns == 0:
            print("you lose")