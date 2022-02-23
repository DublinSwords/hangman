# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 
#words picked for guess
words = ['python', 'program']

picked = random.choice(words)
#right empty list and wrong empty list
right = []
wrong = []
#While loop with if statment 
while True:
    """If user will guess a letter on the screen wil appear Right message 
    if user will guess wrong letter on the screen will appear wrong message"""
    guess = input("Guess a letter")

    if guess in picked:
        right.append(guess)
        print("Right:" ,right)
    else:
        wrong.append(guess)
        print("Wrong:" ,wrong)