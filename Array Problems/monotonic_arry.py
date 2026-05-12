arr = [6,5,4,4]

n = len(arr)

incr = all(arr[i] <= arr[i+1] for i in range(n-1))
decr = all(arr[i] >= arr[i+1] for i in range(n-1))

print(incr or decr)