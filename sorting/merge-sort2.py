"""
** MOST of the EFFICIENT sorting algorithm and based on DIVIDE, CONQUER
   and COMBINE technique.

- DIVIDE the array into two Halves Repeat this step RECURSIVELY!!
- Sort each half.
- Merge the sorted halves back together.

Repeat above steps RECURSIVELY!! 

Properties of the Merge Sort Algorithm
--------------------------------------
1. Based on DIVIDE & CONQUER
2. RECURSIVE
3. STABLE
4. Not an IN-PLACE Algorithm
5. Time Complexity:
        - Worst-case = 0(nlog(n))
        - Best-case = 0(nlog(n))
        - Average-case = 0(nlog(n))
"""
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + 1]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k +=  1

    while j < n2:
        arr[k] = R[j]
        j +=  1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr

arr = [3,1,4,2]
sorted_list = mergeSort(arr, 0, len(arr) - 1 )
print(f"Original List: {arr}")
print(f"Sorted List: {sorted_list}")
