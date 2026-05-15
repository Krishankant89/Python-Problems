def recursion_reversal(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + recursion_reversal(lst[:-1])

n = int(input("Enter the size of array:"))

lst = []

for i in range(n):
    x = int(input("Enter the elements:"))
    lst.append(x)
    
result = recursion_reversal(lst)
print(result)