# Bubble sort in Python
numbers = [10, 2, 8, 34, 6, 18]

# Create swapped flag, set to true in order to enter the main
# Loop
swapped = True
# While elements have been swapped in the last pass,
# Check elements again
while swapped == True:
    # Reset swap to False
    swapped = False
    # Do a pass in the list
    for index in range(1, len(numbers)):
        # Is current number lower than previous one?
        if numbers[index] < numbers[index - 1]:
            # Swap them
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            # If a swap has happened, flag it up
            swapped = True

print(numbers)