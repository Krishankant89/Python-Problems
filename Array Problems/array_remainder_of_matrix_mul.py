def find_remainder(arr,n):
    result = 1
    
    for num in arr:
        result = (result * num) % n
        
    return result


size = int(input("enter the size of array:"))

arr = []

for i in range(size):
    x = int(input("Enter the elements:"))
    arr.append(x)
    
n = int(input("Enter the number to divide the array:"))

print(find_remainder(arr,n))