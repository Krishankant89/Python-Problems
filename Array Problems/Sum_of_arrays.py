def sum_of_array(arr1, arr2):
    n = min(len(arr1),len(arr2))
    result = []
    for i in range(n):
        result.append(arr1[i] + arr2[i])
        
    if len(arr1) > len(arr2):
        for i in range(n, len(arr1)):
            result.append(arr1[i]) 
    else:
        for i in range(n, len(arr2)):
            result.append(arr2[i])  
    return result
arr1 = [1,2,3,4]
arr2 = [5,6,7,8]

print(sum_of_array(arr1, arr2))


"""
def largest_number(arr):
→ Defines a function named largest_number that takes one parameter, arr, which is expected to be a list of numbers.
largest = arr[0]
→ Initializes a variable called largest with the first element of the list. This acts as the starting "current maximum" to compare against.
for i in range(1, len(arr)):
→ Starts a loop that iterates through list indices from 1 to len(arr) - 1. We skip index 0 because we already used it to set our initial largest.
if arr[i] > largest:
→ For each element, checks if the current number (arr[i]) is greater than the value currently stored in largest.
largest = arr[i]
→ If the if condition is true, updates largest to this new, bigger number. This ensures largest always holds the highest value encountered so far.
return largest
→ Once the loop finishes checking every element, the function returns the final value of largest.
arr = [3,7,84,56]
→ Creates a list of integers to test the function.
print(largest_number(arr))
→ Calls the function with arr, receives the returned value, and prints it. The output will be 84.


"""
