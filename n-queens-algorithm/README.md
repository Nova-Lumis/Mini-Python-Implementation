# N-Queens Algorithm
## Description
Search for all possible matrix that makes the queen cannot capture another queen
For example in 4x4 matrix
`[1, 3, 0, 2]` can be accepted since:
```
* Q * *
* * * Q
Q * * *
* * Q *
```
So, There isn't any queen that can meet each other at same row, column, and diagonal.


The solution:
1. Create an adjacent list from the matrix that contains all possible position.

2. On the triggered function (after recursive), search if the possibilities has the same value. Ex. [0,0,1,2] is false since 0 happened 2 times (means queen on the same row)

The formulas used in here is:
...
            for i in range(len(current_matrix) - 1):
                for j in range(len(current_matrix) - (i+1)): 
...

This one is called since we also have to check `matrix[0] == matrix[2]` which is possible by using nested loop. 

We also doesn't want the matrix to loop back aka, checking `matrix[1] == matrix[0]` again. Hence: the j index is added with i. Addition of +1 is the consequences of the index i and j that start from 0.

...
                    if current_matrix[i] == current_matrix[(j+1)+i)]: 
                        return # the matrix cannot have a same number, hence the append method is not called.
...


3. Search for diagonal possibilities.
The key point in searching diagonal possibilities is that the queen exist within a step for each index.

- For example in 3x3 matrix of:
`[0,(any number),2]`,
In here, `matrix[2] = 2 and matrix[0] = 0`.  
The value difference of `matrix[2]-matrix[0] = 2`, also the gap between the index is `[2]-[0] = 2`. The result of two calculation is same (= 2). This means, queen exist on diagonal, and it is true since:
```
Q**
***   (diagonal Q)
**Q
```
This possibilities then removed.

- Another example in 4x4 matrix
`[3,(any number),1,(any number)]`
In here, `matrix[0] = 3 and matrix[2] = 1` -> `matrix[0]-matrix[2] = 3-1 = 2`, also index gap is `[0]-[2] = -2`. The -2 can be change into abs[2], hence why the formula used in the program become absolute.
 
Since the result is the same, it means Queen exist on diagonal. and it is also true since:
```
***Q
****  (diagonal Q)
*Q**
****
```
This possibilities then removed 

From the two example, the formula (without queen) should follows that: `abs(matrix[i]-matrix[j]) != abs([i]-[j])`
In the program, the second term `(abs([i]-[j])` is changed using k_degree, which has the same task.

4. The accepted possibilities that has been filtered by 2 steps earlier added into a new list and displayed as the result.
