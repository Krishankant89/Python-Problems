arr = [6,5,4,4]
n = len(arr)

if n <= 2:
    print(True)
else:
    d = arr[1] - arr[0]
    
    m = True
    
    for i in range(2, n):
        if d == 0:
            d = arr[i] - arr[i -1]
            continue
        if (d > 0 and arr[i] < arr[i - 1]) or (d < 0 and arr[i] > arr[i -1]):
            m = False
            break
    print(m)