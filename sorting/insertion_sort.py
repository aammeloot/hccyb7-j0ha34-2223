# Insertion sort
# From left to right, check numbers are greater than the 
# previous position. If not, push the number backwards
# Until it fits in a position "between" a smaller and
# larger number


numbers = [6, 3, 10, 4, 15, 5]

# Main loop (i) looking at elements from left
# to right. We start with the assumption that
# Element 0 is in the right place.

for i in range(1, len(numbers)):

    # The other loop is using an index 'j'
    # That starts synchronised with 'i'
    j = i

    # While the current number is not the
    # First element
    # AND it's smaller than its predecessor
    # Swap it with its predecessor
    # And decrease j

    while j > 0 and numbers[j-1] > numbers[j]: # test
        # swap
        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        print(numbers)
        # decrease
        j -= 1

print(numbers)