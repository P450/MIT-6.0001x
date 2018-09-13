# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:43:28 2017

@author: Jae Hyun You
"""
low = 0
high = 100

success = False

number = input("Please think of a number between 0 and 100! ")



while not success:
    guess = (low + (high - low)//2)
    print("Is your secret number " + str(guess) + "?")

    letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if letter == 'h':
        high = guess

    elif letter == 'l':
        low = guess

    elif letter == 'c':
        print("Game over. Your secret number was: " + str(guess))
        success = True

    else:
        print("Sorry, I did not understand your input")
        
    
