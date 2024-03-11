print ('hi world')
the_world_is_flat = False
if the_world_is_flat:
    print("Be careful not to fall off!")

    def max_and_min_number_in_list(lst):
    max_num = lst[0]
    min_num = lst[0]
    
    for num in lst:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    
    # Note the order here for the return value
    return (max_num, min_num)

# Testing the function
print(max_and_min_number_in_list([1,2,3,4,5]))  # This should return (5, 1)
print(max_and_min_number_in_list([-1,-4,-5,-7]))  # This should return (-1, -7)
