# Standard linear search algorithm

# Data definitions

fruitlist = ['apple', 'mango', 'banana', 'orange']
s = input('enter a fruit you look for')
found = False
position = 0

# Key algorithm

for counter in range(len(fruitlist)):
    if s == fruitlist[counter]:
        found = True
        position = counter
        break

# Add an output
if found:
    print('Element found position: ', position)
else:
    print('Element not found')

