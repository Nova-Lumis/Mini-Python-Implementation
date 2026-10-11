# Quick Sort Algorithm
## Process
The Process/step of Quick Sort Algorithm in this program is written below:
1. Determine the number of element inside the list. Set it as n.
2. Set i (as loop index) = 0 and j(as passable parameter for swapping) = -1
3. Set the pivot as the last element on the list
4. Use the swapping process:
   1.  if list[i] > pivot: do i += 1 only.
   2.  elif list[i] <= pivot: do j += 1. This condition will be further investigated
   3.  inside the second condition, check if i == j. if False, swap the two values position between list[i] and list [j]
5. The resulted list from swapping process will be distributed into three partition. Create 3 partition (part1, part2, part3) with []
6. Distribute the value according to the requirement below:
   1. part1 is for value less than pivot
   2. part2 is for value equal to pivot
   3. part3 is for value more than pivot
7. Each of these partition contains number and will go through process number 1 again.
8. Add each of the quick sort process using quick_sort(part1) + part2 + quick_sort(part3). Part2 must not have quick_sort called on it
9. Set the condition to break the recursive of quick_sort function, which is n <= 1.

## Additional Notes
<p>
  Note that the Quick Sort Algorithm that is written on the file used more space complexity compared to normal Quick Sort Algorithm (using the `low` and `high` version.
</p>
<p>
  However, since that version, at the time of this program is written, The writer acknowledge its difficulty to comprehend (too abstract). This quick sort program is written using
  the same concept of quick sort algorithm.
</p>

## Concept for First Iter
<p>
  The directory is added with the concept of Quick Sort Algorithm for the first iteration and only first iteration.
  It is added to understand the process beyond the function of `quick_sort()` and its recursive call.
</p>

## References
- https://en.wikipedia.org/wiki/Quicksort
- [Video] https://www.youtube.com/watch?v=WprjBK0p6rw
