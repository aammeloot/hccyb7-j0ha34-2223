# A demo of Strings in Python 3

content = "Python is my favourite subject this year."

print(content)

# You can use strings like you can use arrays
# print(content[start:finish:index])

# Display a single character
print(content[8])
# Display a sub string
print(content[10:16])
# Display all from a character
print(content[10:])
# print the last character
print(content[-1])
print(content[-3])

# Skip every other character
print(content[::2])
# Print in reverse
print(content[::-1])

# Not gonna work because case sensitive
if "python" in content:
    print('It is there')
else:
    print('not there')


