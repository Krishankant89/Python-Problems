def is_anagram(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq = {}
    
    for x in arr1:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    for x in arr2:
        if x not in freq:
            return False
        
        freq[x] -= 1
        if freq[x] < 0:
            return False
    return True
    
n1 = int(input("Enter size of first array:"))
arr1 = list(map(int,input(f"Enter {n1} elements:").split()))

n2 = int(input("Enter size of first array:"))
arr2 = list(map(int,input(f"Enter {n2} elements:").split()))


if len(arr1) != n1 or len(arr2) != n2:
    print("Error : numbers of elements not matching size")
else:
    if is_anagram(arr1, arr2):
        print("Arrays are Anagram")
    else:
        print("Not Anagram")