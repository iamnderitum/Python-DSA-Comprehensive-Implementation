"""
Properties of Bubble Sort Algorithm
------------------------------------
1. Iterative
2. Stable - equivalent elements retain positions after sorting
3. In-place algorithm.
4. Time Complexity:
    - Worst Case - O(n^2)
    - Best Case - O(n)
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) -i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array
    
#print(bubbleSort([5,8,1,3,5,6,5,8]))

#### BEST CASE SCENARIO CODE --> Occurs when array is fully sorted
def bubbleSort2(array):
    for i in range(len(array)):
        num_swaps = 0 #
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                num_swaps += 1

        if num_swaps == 0:# if no swaps, terminate function earlier
            break
        
    return array

print(bubbleSort2([5,8,1,3,5,6,5,8]))

