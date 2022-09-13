thisnames = ["sarah", "james", "michael", "susan", "gerry"]

# Exercise 1

search_term = input('What name do you want to search?')

# Exercise 1
found = False
# Compare search terms with elements
for current_name in thisnames:
    if search_term == current_name:
        # If found flag it and stop the loop
        found = True
        break;

if found:
    print('Yes! name found!')
else:
    print('Name not found!')


# Exercise 5:
newlistwiths = []

for current_name in thisnames:
    if 's' in current_name:
        newlistwiths.append(current_name)

print(newlistwiths)

