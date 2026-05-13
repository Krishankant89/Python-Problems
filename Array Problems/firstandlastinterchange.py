def swap_list(lst):
    if len(lst) > 1:
        lst[0],lst[-1] = lst[-1],lst[0]
    return lst

my_list = [10,20,30,40,50]

print(my_list)
new_list = swap_list(my_list)
print(new_list)