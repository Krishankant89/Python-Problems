def max_min(arr, i = 0, mini=None, maxi=None):
    
    if mini is None:
        mini = arr[0]
        maxi = arr[0]
        
    if i == len(arr):
        return mini,maxi
    
    else:
        if arr[i] < mini:
            mini = arr[i]
            
        if arr[i] > maxi:
            maxi = arr[i]
            
            
    return max_min(arr, i+1, mini,maxi)

arr = [23,4,1,3,5]

minimum, maximum = max_min(arr)

print(f"Min: {minimum}, Max: {maximum}")


'''
if we initalize 'mini' and 'maxi' to 0, our code breaks whenever the array conatins
only negative numbers or only greater numbers than zero.



maxi = 0:

The code looks at -5. Is -5 > 0? No. maxi stays 0.

The code looks at -12. Is -12 > 0? No. maxi stays 0.

The code looks at -3. Is -3 > 0? No. maxi stays 0.

The function returns maxi = 0. But 0 isn't even in your array! The true maximum is -3. Because you initialized to 0, your initial guess was higher than every single number in the data set,
ruining the result.




initialize mini = 0:

The code looks at 85. Is 85 < 0? No. mini stays 0.

The code looks at 92. Is 92 < 0? No. mini stays 0.

The code looks at 78. Is 78 < 0? No. mini stays 0.

The function returns mini = 0. But the lowest actual test score was 78. 
Because 0 is smaller than any valid score, 
the function never updates mini.

Using None acts as a flag that says: "We haven't looked at the data yet."

As soon as the function starts, it sees None and immediately executes

'''