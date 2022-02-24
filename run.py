# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 

# another file from where I am importing parts
from hangman_parts import parts

# importing sleep so our program can delay for .5 seconds
from time import sleep

# list of words from waht i can cchouse
words = ['python', 'program']

picked = random.choice(words)

#print the message and number of letters
print("The word has", len(picked), "letter")

# right empty list and wrong empty list
right = ['_'] * len(picked)
wrong = []

# Function will update my right list with underscor 
def update():
    for i in right:
        print(i, end = ' ')
    print()
print('Let me think of a word')

# Function will delay our program for .5seconds 
def wait():
    for i in range(5):
        print('.', end = ' ')
        sleep(.5)
    print()

wait()

update()
parts(len(wrong))


# While loop with if statment 
while True:
    """ In case If user will guess a letter on the screen will not appear a hangman
    in case if user will guess wrong letter on the screen will appear parts of hangman"""
    print("======================")
    guess = input("Guess a letter:")
    print('Let me check')
    wait()

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index +=1
        update()
    else:
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
        else:
            print("You already guessed that")
        print(wrong) 
    if len(wrong) > 3:
        print("You lose")
        print('I picked', picked)
        break
    if '_' not in right:
        print("You win!:)")
        break