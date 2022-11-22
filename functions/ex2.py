'''
We will work through this exercise in class and run it in debug so we can see what happens
Write a program which creates a list of random numbers then outputs the list of random numbers.
We have done something similar before! But this time:
•	The main code will welcome the user and tell them what will happen
•	We will write a function called create_list to create the list of random numbers
•	This function will take no parameters, and will return the list it has created
•	This function will be called by the Main code, and after it has completed, 
    the Main code will have the new list and can print out the numbers in it
Let's try it together
'''

import random

def create_list():
    # Create a list of 10 numbers
    numbers = []
    for index in range(10):
        random_number = random.randint(1,100)
        numbers.append(random_number)
    return numbers
