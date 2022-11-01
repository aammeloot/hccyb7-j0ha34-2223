import numbers



# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        print('attempt')
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [1,3,10,11,15,22,28,29,35,38,48,49,54,58,59,61,65,68,74,78,80,81,86,92,101,119,126,141,142,147,151,153,162,164,169,172,174,176,177,186,189,192,199,207,215,220,231,232,236,243,247,250,260,266,271,274,275,277,280,281,284,285,289,291,293,301,311,326,332,337,345,353,373,390,394,395,397,403,414,415,417,427,428,432,433,436,437,449,453,459,465,466,469,475,479,481,483,488,491,500]
x = 437
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")