# Create an array of five different names
# Create a loop running five times

# Create an empty list
name_list = []

for index in range(5):   # Repeat five times
    name = input('Enter a name')
    name_list.append(name)

# Print the whole list at once
print(name_list)

# You can use a loop to display individual elements
for single_name in name_list:
    print('I like', single_name, '!')

# Another way to do a loop:
counter = 0
while counter < 5:
    print(name_list[counter])
    counter = counter + 1
    
