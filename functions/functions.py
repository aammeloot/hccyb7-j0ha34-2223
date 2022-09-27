# Greet user
def greetUser():
    username = input('What is your name?')
    print('Hello,', username+'!')

# Procedure: takes data in and does something with it
def greetUserWithName(username):
    print('Hello,', username + '!')

# Function: properly takes in one or more parameters
# And returns a value (or more than one)
def add(a, b):
    c = a + b
    return c

# Call the first example
# greetUser()

# Call the second example
greetUserWithName('Aurelien')
greetUserWithName('Lorna')

# Another was to call the second example
students = ['Stewart', 'Ewan', 'Margo', 'Kyle', 'Lauren']
for studentName in students:
    greetUserWithName(studentName) # Parameter passing by value

# Third example, add
add(10, 5)
add(17, 5)
# There's no output, you need to recover the result 
# either in a variable or another construct
print(add(10,5))
c = add(17,5)
print(c)
