# Selection sort algorithm
testing_list = [5, 7, 9, 3, 2, 1, 5, 9, 7]

# function of selection sort 
def selection_sort(testing_list):
    # Variable
    n = len(testing_list) # total element on the list
    keep_looping = True # loop condition
    j = 0 
    # j, is variable for setting smallest value and searching range in the loop
    step = 0 # number of loop executed

    while keep_looping:
        # # Finding smallest value
        smallest_value = testing_list[j]
        value_found = False

        # smallest_value = testing_list[0]
        for i in range(j, n):
            if testing_list[i] < smallest_value:
                smallest_value = testing_list[i]
                value_found = True
        
        # Condition
        if value_found:
            # smallest_value_index, the index search should be in range [j:n] and added with j
            # this can solve the problem when testing list has a same number
            smallest_value_index = testing_list[j:n].index(smallest_value) + j

            # Swapping the two value based on index
            testing_list[j], testing_list[smallest_value_index] = testing_list[smallest_value_index], testing_list[j]

        j = j + 1
        step += 1

        # displaying the process
        # print(f"{testing_list},  {step}")

        # Condition to break
        if j >= n:
            keep_looping = False
    
    return testing_list


# Displaying the result
print("--------------")
print(selection_sort(testing_list))
