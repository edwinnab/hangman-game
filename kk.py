import random
import time
ages = ["twenty", "forty"]
playgame = True
guess = []
guess_list = []
category = ""
#introduce the game to users 
print("welcome to hang man let us plaaayyyyy")
time.sleep(1)
print(r"enter 'a' to start")
time.sleep(1)
#logic for playing
while True:
    if category.lower() == "a":
        secretword = random.choice(ages)
        break
    elif category.lower() == "x":
        print("Bye thanks for trying")
        playgame = False
    else:
        print("kindly pick 'a' to start and 'x' to cancel the game")
    if playgame:
        secret_list = list(secretword)
        attempts = (len(secretword) + 2)
        def guessed():
            print("your guessed letter is: " + "".join(guess_list))
        for n in secret_list:
            guess_list.append("_")
        guessed()
        print("your total number of guess is: ", attempts)
        while True:
            print("Guess a letter: ")
            letter = input()
        if letter in guess:
            print("you have already guessed this letter.")
        else:
            attempts -= 1
            guess.append(letter)
        if letter in secret_list:
            print("nice guess")
            if attempts > 0:
                print("you have", attempts, "guess left!")
        for i in range(len(secret_list)):
            if letter == secret_list[i]:
                letterindex = i
                guess_list[letterindex] = letter.lower()
        guessed()


    