def max_min(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
                      
        if arr[i] > maxi:
            maxi = arr[i]
    return mini,maxi
arr = [23,1,45,67]
minimum, maximum = max_min(arr)
print(f"Min: {minimum}, Max: {maximum}")