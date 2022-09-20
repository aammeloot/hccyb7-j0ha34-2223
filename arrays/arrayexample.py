# Demonstration of arrays (lists)
# Base array: lecturers

tutors = ['Arthur', 'Jim', 'Aurelien']

# Print a description
print(tutors)

# Print a specific value
print(tutors[1])

# Add a new person at the end of the list
tutors.append('Mark')
print(tutors)

# Replace a specific tutor with another one
tutors[1] = 'Lorna'
print(tutors)

# Remove aurelien
tutors.pop(2)
print(tutors)
tutors.insert(0, 'Aurelien')
print(tutors)

