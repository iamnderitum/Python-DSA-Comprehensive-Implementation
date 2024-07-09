"""
** What is a Max-Heap? Its a COMPLETE binary tree in which each
    NODE is either greater than or equal to its children.

- Transform the array into a Max-Heap
        build_max_heap(arr)
            heapify(arr, n, i)

- Swap MAXIMAL element with the LAST
- Reconstruct the Max-Heap
- Continue according to this principle

Properties of the Heap Sort Algorithm
1. Iterative(but heapify is recursive).
2. NON-ADAPTIVE.
3. NOT STABLE
4. IN-PLACE algorithm
5. Time Complexity:
        - Worst-case = 0(n.log(n))
        - Best-case = 0(n.log(n))
        - Average-case = 0(n.log(n))  
"""

## CODE FOR BUILD_MAX_HEAP & HEAPIFY
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildMaxHeap(arr):
    n = len(arr)
    for j in range(n//2 - 1, -1, -1):
        heapify(arr, n, j)


## CODE FOR HEAP SORT
def heapSort(arr):
    n = len(arr)
    buildMaxHeap(arr)
    for k in range(n - 1, 0, -1):
        arr[0], arr[k] = arr[k], arr[0]
        heapify(arr, k, 0)

    return arr
arr = [4,2,6,5,1,3,9]
print(heapSort(arr))