print("n-queen problems: \n")

n = 5  # dimension, adjacent list matrix for every possible queen position 
all_possible = []

def generate_combinations(current_matrix):
    
    # When the matrix reached n, this return possibilities triggered
    if len(current_matrix) == n:
        # check whether same row has same number
        for i in range(len(current_matrix) - 1):
            for j in range(len(current_matrix) - (i+1)):
                if current_matrix[i] == current_matrix[j+(i+1)]:
                    return
        
        # check whether a diagonal has a value of k_degree(whether queen exist). 
        for i in range(len(current_matrix) - 1):
            k_degree = 0
            for j in range(len(current_matrix) - (i+1)):
                k_degree += 1
                if (abs(current_matrix[i] - current_matrix[j+(i+1)]) == k_degree):
                    return


        all_possible.append(current_matrix)
        return

    # Recursive to add to all possible matrix
    for val in range(n):
        generate_combinations(current_matrix + [val])

# Start the process using an empty list
generate_combinations([])

print(f"Total combinations for N={n}: {len(all_possible)}")
print(all_possible)
