"""
- Select the smallest element from the unsorted part of the array and place it at the 
first position.
- Also referred to as MinSort or MaxSort.

Properties of Selection Sort:
-----------------------------
1. Iterative - uses 2 for loops.
2. Instable - Can change the order of equivalent element after sorting.
3. In-place algorithm - performs operations on the input array.
4. Time Complexity:
    - Worst Case - 0(n^2)
    - Best Case - 0(n^2)
    - Average Case - 0(n^2)
"""
def selectionSort(array):
    n = len(array)
    for ind in range(n):
        min_index = ind
        for j in range(ind + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])

    return array

print(selectionSort([4,2,6,5,1,3]))