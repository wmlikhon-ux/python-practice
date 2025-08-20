import os
os.system('cls')
import random

select_randtxt = random.randint(1, 100)

print("🎲 Guess the Number Game 🎲")
print("I have selected a random number between 1 and 100.")

while True:
    guess = int(input("Enter your guess (1-100): "))
    if guess < select_randtxt:
        print("Too low! Try again.")
    elif guess > select_randtxt:
        print("Too high! Try again.")
    elif guess == select_randtxt:
        print("Congratulations! You've guessed the number!")
        break
