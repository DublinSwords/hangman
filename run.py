# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 

words = ['python', 'program']

picked = random.choice(words)

right = []
wrong = []

while True:

    guess = input("Guess a letter")

    if guess in picked:
        right.append(guess)
        print("Right:" right)
    else:
        wrong.append(guess)
        print("Wrong:" wrong)