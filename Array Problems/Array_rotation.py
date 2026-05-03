def left_rotate(arr, k):
    n = len(arr)
    k = k % n   # handle k > n
    
    result = []
    
    # Step 1: take elements from k → end
    for i in range(k, n):
        result.append(arr[i])
    
    # Step 2: take first k elements
    for i in range(0, k):
        result.append(arr[i])
    
    return result


arr = [1,2,3,4,5]
print(left_rotate(arr, 2))