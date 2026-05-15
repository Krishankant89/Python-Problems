def sum_of_elements(arr):
    res = 0
    i = 0
    while i < len(arr):
        res += arr[i]
        i += 1

    return res
n = int(input("Enter the size of array:"))

arr = []

for i in range(n):
    x = int(input("Enter the elements:"))
    arr.append(x)
    
print(arr)
result = sum_of_elements(arr)
print(result)