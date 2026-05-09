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
