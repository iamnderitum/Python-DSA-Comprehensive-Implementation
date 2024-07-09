"""
*** A Commonly used Recursive algorithm for sorting, which is based on the divide
    and conquer technique.

- Pick a pivot element x of the array.
- Use the element x to divide the array into two sub-arrays:
    + The left sub-array contains all elements y with: y <= x.
    + The right sub-array contains all elements y with: x < y.
- The pivot element x is then at the correct position in the array, and we have to 
  sort sub-arrays

  Properties of the Quick Sort :
  -----------------------------
  1. Based on Divide and Conquer.
  2. Recursive.
  3. Not Stable.
  4. In-Place algorithm
  5. Time Complexity:
        - Worst-case - 0(n^2)
        - Best-case - 0(n.log(n))
        - Average-case - 0(n.log(n))

- NOTE: For very large arrays, Its recommended you choose the PIVOT randomly.
        --> Choosing a random pivot minimizes the chance to encounter the Worst Case
"""

import random
## PARTITION CODE
def partation(array, low, high):
    piv_index = random.randrange(low, high)
    pivot = array[piv_index]
    (array[high], array[piv_index]) = (array[piv_index], array[high])

    #pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
#### QUICK SORT CODE
def quickSort(array, low, high):
    if low < high:
        pi = partation(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

    return array

#array, low, high = [4,2,6,5,1,3,9], 0, 6
#print(quickSort(array, low, high))

## ARGUMENT UNPACKING

array_low_high_values = [4,2,6,5,1,3,9], 0, 6
print(quickSort(*array_low_high_values))