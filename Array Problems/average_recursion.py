def find_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + find_sum(arr[1:])

lst = int(input("Enter the size of array:"))

arr = []

for i in range(lst):
    value = int(input(f"Enter the elements {i}:"))
    arr.append(value)
    
average = find_sum(arr) / len(arr)

print("The average of numbers are",average)