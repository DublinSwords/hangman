# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random 

# words picked for guess
words = ['python', 'program']

picked = random.choice(words)
print("The word has", len(picked), "letter")

# right empty list and wrong empty list
right = ['_'] * len(picked)
wrong = []

# Function will update my right list
def update():
    for i in right:
        print(i, end = ' ')
    print()
update()


# While loop with if statment 
while True:
    """ In case If user will guess a letter on the screen wil appear Right message 
    in case if user will guess wrong letter on the screen will appear wrong message"""
    print("======================")
    guess = input("Guess a letter:")

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
        else:
            print("You already guessed that")
        print(wrong) 
    if '_' not in right:
        print("You win!:)")
        break