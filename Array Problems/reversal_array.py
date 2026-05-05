def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
def left_rotation(arr, k):
    n = len(arr)
    k = k % n
    
    reverse(arr, 0, k - 1)
    
    reverse(arr, k, n -1)
    
    reverse(arr, 0, n - 1)
    
    
    return arr


n = int(input("Enter the size of array:"))

arr = []

for i in range(n):
    x = int(input("enter the elements:"))
    arr.append(x)
    
k = int(input("enter the number of rotaions:"))

result = left_rotation(arr, k)

print("Array after left rotation:", result)