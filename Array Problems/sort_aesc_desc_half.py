def sorting(arr):
    
    for i in range(len(arr)):
        for j in range(i +1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]

    mid = len(arr) //2
    
    for i in range(0, mid):
        print(arr[i], end = " ")
        
    for i in range(len(arr) -1, mid-1,-1):
        print(arr[i], end=" ")
        
arr = [7,6,2,4,8,5,9]

result = sorting(arr)

print(result)