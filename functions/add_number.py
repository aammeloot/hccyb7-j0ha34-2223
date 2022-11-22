''' 
1.	Create a function to add two numbers
We will work through this exercise in class and run it in debug so we can see what happens
Write a program which asks the user for two numbers, adds them together, then tells the user the answer. We have done similar before! But this time:
•	The user interaction (asking for the numbers and outputting the result) happens in the main function
•	The adding of the two numbers happens in a function called add
•	The Add function will take the two numbers as parameters and return the results
•	The Add function will be called in the Main code, and the result will be returned to the main code
       Let's try it together
'''

def add(num1, num2):
    return num1 + num2



number1 = int(input("Select a number"))
number2 = int(input("Select another number"))

total = add(number1, number2)

print(total)
