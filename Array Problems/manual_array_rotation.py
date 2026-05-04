def left_rotation(arr,k):
    n = len(arr)
    k = k % n
    
    result = []
    
    for i in range(k, n):
        result.append(arr[i])
    
    for i in range(0, k):
        result.append(arr[i])
        
    return result

n = int(input("enter the size of array:"))

arr = []
for i in range(n):
    x = int(input("Enter the elements:"))
    arr.append(x)
    
k = int(input("Enter number of rotations:"))

rotated = left_rotation(arr, k)

print("Rotated array:", rotated)



'''
🔹 Split the Array
Original:   [1, 2, 3, 4, 5]
Index:       0  1  2  3  4
k = 2

Split at index k:

First half  = [1, 2]        → index 0 to k-1
Second half = [3, 4, 5]     → index k to n-1
🔹 Combine (Swap Order)
Rotated = Second half + First half
        = [3, 4, 5] + [1, 2]
        = [3, 4, 5, 1, 2]
        
“We use k % n because array rotation is cyclic. Rotating more than n times is redundant, so we reduce it to the minimum effective rotations.”

🔹 Edge Cases it handles
1. k > n
k = 12, n = 5
k % n = 2
2. k = n
k = 5, n = 5
k % n = 0  → no rotation
3. k = 0
k % n = 0 → no rotation
'''