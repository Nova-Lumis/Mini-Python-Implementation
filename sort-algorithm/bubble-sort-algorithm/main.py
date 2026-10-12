# Bubble sort method
testing_list = [5, 7, 9, 3, 2, 1, 5, 9, 9.5]

# variable...
n = len(testing_list)
keep_looping = True

while keep_looping:
    loop_found = False
    for i in range(n-1):
        if testing_list[i] > testing_list[i+1]:
            # swapping the two values
            testing_list[i+1], testing_list[i] = testing_list[i], testing_list[i+1]
            loop_found = True
    
    # Each looping results
    print(testing_list)

    # Condition to break
    if not loop_found:
        keep_looping = False
