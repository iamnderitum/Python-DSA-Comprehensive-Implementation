"""
- Sorting by the insertion of items into the sorted array part.
- First element in the array describels a sorted sub-array.
- Insert elements from the unsorted sub-array into the correct position
  in the sorted sub-array

  Properties of the Insertion Sort
  --------------------------------
  1. Iterative
  2. Stable - Equivalent element retain their relative position after the application 
     of Insertion Sort.
  3. In-place Algorithm - performs all operations on the input array.
  4. Online agorithm . In the following manner.
        - It can process its inputs piece by piece in a serial fashion in the order
        that the input is fed to the algorithm without having the entire input available
        from the start. This is the case because the algorithm considers one input 
        element per iteration and produces a partial solution without the consideration
        of future elements.

   5. Time Complexity:
        - Worst-case - 0(n^2)
        - Best-Case - 0(n)
        - Average-case - 0(n^2)
"""
from typing import Dict ,List
def insertionSort(array) -> Dict:
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j]> key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
array = [4,2,6,5,1,3]
print("Original array: ",array)
print("Sorted List: ",insertionSort(array))

