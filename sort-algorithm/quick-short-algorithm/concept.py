# -------------------------- MAIN CONCEPT ---------------------
"""
First iteration only.
"""
# testing list
testing_list = [4, 7, 9, 2, 5, 1]

# set i and j, and pivot (last_element)
i = 0
j = -1
pivot = testing_list[len(testing_list) - 1]


for i in range(len(testing_list)):
    # Condition for quick sort swapping
    if testing_list[i] > pivot:
        i = i+1
    elif testing_list[i] <= pivot:
        j = j+1
        if not i == j:
            print(testing_list[j])
            a = testing_list[i]
            b = testing_list[j]
            testing_list[i] = b
            testing_list[j] = a
        i = i+1


print(testing_list)

#Create partition
part1 = []
part2 = []
part3 = []

"""
part1 is for value less than pivot
part2 is for value equal to pivot
part3 is for value more than pivot
"""
for i in range(len(testing_list)):
    if testing_list[i] < pivot:
        part1.append(testing_list[i])
    elif testing_list[i] == pivot:
        part2.append(testing_list[i])
    elif testing_list[i] > pivot:
        part3.append(testing_list[i])

print(part1, part2, part3)

# -------------------------- MAIN CONCEPT ---------------------
# # ------------------MAIN CONCEPT--------------------------
