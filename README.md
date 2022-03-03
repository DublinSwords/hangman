# Hangman 
Hangman is a Python terminal game, a player's objective is to identify a hidden words. In each round, the player guesses a letter of the alphabet, if it is present in the word all instances are revealed, otherwise one of the hangman's body parts is drawn in on the gibbet. The game ends in a win if the word entirly revealed by correct guesses, and ends in loss if the hangman's body is completely revealed in stead. Too assist the player, a visible record of all guessed letters is typically maintained. 
The network receives as input a representation of the word (total number of characters, the identify of any revealed) as well as a list of which letters have been guessed so far. 

![](images/image1.png)