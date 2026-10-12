# Quick sort algorithm
"""
quick_sort algorithm:
function quick_sort accept parameter: list of integer number
and return its sorted list using quick sort algorithm

quick sort algorithm process:
1. Determine the number of element inside the list. Set it as n.
2. Set i (as loop index) = 0 and j(as passable parameter for swapping) = -1
3. Set the pivot as the last element on the list
4. Use the swapping process:
-if list[i] > pivot: do i += 1 only.
-elif list[i] <= pivot: do j += 1. This condition will be further investigated
-inside the second condition, check if i == j. if False, swap the two values position between list[i] and list [j]
5. The resulted list from swapping process will be distributed into three partition. Create 3 partition (part1, part2, part3) with []
6. Distribute the value according to the requirement below:
- part1 is for value less than pivot
- part2 is for value equal to pivot
- part3 is for value more than pivot
7. Each of these partition contains number and will go through process number 1 again. 
8. Add each of the quick sort process using quick_sort(part1) + part2 + quick_sort(part3). Part2 must not have quick_sort called on it
9. Set the condition to break the recursive of quick_sort function, which is n <= 1.
"""

# FUNCTION************************************************
def quick_sort(int_list):
    # n is the number of element in the list
    n = len(int_list)

    # Condition for funtion to break. It has to meet n <= 1
    if n <= 1:
        return int_list

    # Set i and j, and pivot as last element in the list
    # i is the index for looping the int_list, j is the index where the swap process takes place
    i = 0
    j = -1
    pivot = int_list[n - 1]

    # Swapping process. 
    for i in range(n):
        if int_list[i] > pivot:
            i = i+1
        # The condition, elif, meet the requirement of swapping the index of the two values (when i != j)
        elif int_list[i] <= pivot:
            j = j+1
            if not i == j:
                a = int_list[i]
                b = int_list[j]
                int_list[i] = b
                int_list[j] = a
            i = i+1

    # Checking the process of quick sort (CAN BE IGNORED)
    print(int_list)

    # Create partition
    """
    The partition has to meet these points:
    - part1 is for value less than pivot
    - part2 is for value equal to pivot
    - part3 is for value more than pivot
    """
    part1 = []
    part2 = []
    part3 = []

    # Adding the partition according to the requirements
    for i in range(len(int_list)):
        if int_list[i] < pivot:
            part1.append(int_list[i])
        elif int_list[i] == pivot:
            part2.append(int_list[i])
        elif int_list[i] > pivot:
            part3.append(int_list[i])
    
    # Displaying the partition (CAN BE IGNORED)
    print(part1, part2, part3)

    # Call the quick_sort function on each of the partition until each partition meets n <= 1.
    int_list = quick_sort(part1) + (part2) + quick_sort(part3)

    # return the modified list
    return int_list


## MAIN
# Testing list
testing_list = [1, 1, 1, 9, 10, 5, 9, 30, 15, 77, 21, 9]
print("\nThe original unsorted list is:\n")
print(f"{testing_list}\n")
print("\nThe sorted list is:\n")
print(quick_sort(testing_list))




