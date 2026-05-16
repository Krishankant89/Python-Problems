def multiply_elements(arr):
    
    if len(arr) == 0:
        return 1
    
    return arr[0] * multiply_elements(arr[1:])

a  = int(input("Enter the size of array:"))

arr = []

for i in range(a):
    val = int(input("Enter the elements:"))
    arr.append(val)

result =  multiply_elements(arr)
print(result)