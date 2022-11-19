import random
# library that we use in order to choose
# on random words from a list of words
 
name = input("\nHello! and Welcome To The Hangman Game!\nWhat is your name?\n ")
# Here the user is asked to enter the name first
print("\nRULES:-")
print("1.You will get 6 chances to guess a word.")
print("2.If the entered character is right, it will be shown on the screen.")
print("3.If it is wrong, 1 chance will be reduced.\n") 
print("Good Luck !", name)
 
words = ['foxmula', 'computer', 'microsoft', 'programming',
         'python', 'mathematics', 'cricket', 'condition',
         'elephant', 'google', 'board', 'software']
 
# Function will choose one random
# word from this list of words
word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
# any number of turns can be used here
chance = 6
 
 
while chance > 0:
     
    # counts the number of times a user fails
    fail = 0
     
    # all characters from the input
    # word taking one at a time.
    for char in word:
         
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
            # for every failure 1 will be
            # incremented in failure
            fail += 1
             
 
    if fail == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("Congratulations! You have won the Hangman Game!")
         
        # this print the correct word
        print("The word is: ", word)
        break
     
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("Guess a character:")
     
    # every input character will be stored in guesses
    guesses += guess
     
    # check input with the character in word
    if guess not in word:
         
        chance -= 1
         
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
         
        # this will print the number of
        # turns left for the user
        print("You have", + chance, 'more guesses\n')
         
        
        if chance == 0:
            print("You have lost The Hangman Game.\n\nThe word was",word)
            print("\nBetter luck next time!")