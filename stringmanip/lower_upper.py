# Case manipulation

content = input('Enter a long-ish sentence: ')

print('lower case:', content.lower())
print('UPPER CASE:', content.upper())
print('Capitalised:', content.capitalize())
print('Title Case:', content.title())

# When you search for a substring, make sure you work in
# The same case

print('Enter a string you want to find in', content)

searchterm = input('Enter your term')

if(searchterm.lower() in content.lower()):
    print('Found it')
else:
    print('Not found')

# Change the case, and save it
content = content.upper()
