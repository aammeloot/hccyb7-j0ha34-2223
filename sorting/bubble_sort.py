# Bubble sort in Python
array = [10, 2, 8, 34, 6, 18]

for pass_number in range(len(array)):
    # Move larger number to the end
    for counter in range(1, len(array)):
        # Compare them, if in wrong order, swap them
        if array[counter - 1] > array[counter]:
            array[counter], array[counter-1] = array[counter-1], array[counter] # Don't try in another language


        # Intermediate printout of the array
        print(array) 



