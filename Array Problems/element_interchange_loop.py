lst = int(input("Enter the size of array"))

arr = []

for i in range(lst):
    x = int(input("Enter the elements:"))
    arr.append(x)
    
print("Before Swapping",arr)

n = len(arr)

for i in range(n):
    if i == 0:
        temp = arr[i]
        arr[i] = arr[n-1]
        arr[n-1] = temp
print("After swapping",arr)