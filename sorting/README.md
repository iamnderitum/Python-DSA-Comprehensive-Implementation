# SORTING ALGORITHMS

### 1. BUBBLE SORT.
##### 📌 Technique: Comparison Based
##### 📐 Stability: Yes(Preserves the relative order of equal elements)
##### ☢️ Recursive: No (Typically implemented iteratively)
##### 💾 In-place: Yes (requires only a costant amount of additional space)
##### 📜 Description: Bubble Sort repeatedly steps trhough the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.


##### 🛠️ 🗜️ Implementation 

    1. Start at the beginning of the list.
    2. Compare the first two elements.
    3. If the first element is greater than the second, swap them.
    4. Move to the next pair of elements and repeat step 3.
    5. Continue until the end of the list.
    6. Repeat the entire process for the next pass, ignoring the last sorted elements.
    7. Continue until no swaps are needed in a pass.

##### ⏳ ⏰ Time Complexity.
    - Best Case: 0(n) (When the list is already sorted)
    - Average Case: 0(n^2)
    - Worst Case: 0(n^2)


### 2. SELECTION SORT.
##### 📌 Technique: Selection Based
##### 📐 Stability: No (Does not Preserve the relative order of equal elements)
##### ☢️ Recursive: No (Typically implemented iteratively)
##### 💾 In-place: Yes (requires only a costant amount of additional space)
##### 📜 Description: Selection sort divides the list into a sorted and an unsorted region. It repeatedly selects the smallest(or largest) element from the unsorted region and moves it to the end of the sorted list.

##### 🛠️ 🗜️ Implementation
    1. Start with the first element as the minimum.
    2. Compare this element with the rest of the elements to find the smallest element.
    3. swap the smallest element with the first elemt.
    4. Move the boundary of the sorted and unsorted regions by one element to the right
    5. Repeat setps 1 - 4 for the remaining unsorted elements.

##### ⏳ ⏰ Time Complexity
    - Best Case: 0(n^2)
    - Average Case: 0(n^2)
    - Worst Case: 0(n^2)

### 3. INSERTION S0RT

##### 📌 Technique: Insertion-based
##### 📐 Stability: Yes (Preserves the relative order of equal elements)
##### ☢️ Recursive: No (Typically implemented iteratively)
##### 💾 In-place: Yes (requires only a costant amount of additional space)
##### 📜 Description: Insertion Sort builds the final sorted list one at a time. It removes an element from the input data, finds the location it belongs within the sorted list, and inserts it there. Its an online algorithm.


##### 🛠️ 🗜️ Implementation
    1. Start with the second element as the key.
    2. Compare the key with elements before it.
    3. Shift elements one position to the right to make space for the key if needed.
    4. Insert the key at its correct postion.
    5. Move to the next element and repeat steps 2-4 until the list is sorted.

##### ⏳ ⏰ Time Complexity.
    - Best Case: 0(n) (When the list is already sorted)
    - Average Case: 0(n^2)
    - Worst Case: 0(n^2)


### 4. QUICK SORT

##### 📌 Technique: Divide & Conquer
##### 📐 Stability: No (Does not Preserve the relative order of equal elements)
##### ☢️ Recursive: Yes (naturally recursive)
##### 💾 In-place: Yes (can be implemented in-place, although additional space may be required for recursion stack)
##### 📜 Description: Quick Sort  selects a "pivot" element and partitions the array into two sub-arrays: Elements less than the pivot and elements greater than the pivot. It then recursively sorts the sub-arrays.

##### 🛠️ 🗜️ Implementation
    1. Choose a pivot element from the array.
    2. Partition the array into two sub-arrays: Elements less than the pivot and elements greater than the pivot.
    3. Recursiveley apply the same steps to the sub-arrays.
    4. Combine the sorted sub-arrays and the pivot into a single sorted array.

##### ⏳ ⏰ Time Complexity
    - Best Case: 0(n log n)
    - Average Case: 0(n log n)
    - Worst Case: 0(n^2) (when the pivot selection is poor, e.g., always choosing the smallest or largest element)


### 5. MERGE SORT

##### 📌 Technique: Divide & Conquer
##### 📐 Stability: Yes (Preserves the relative order of equal elements)
##### ☢️ Recursive: Yes (naturally recursive)
##### 💾 In-place: No (requires additional space proportional to the size of the array for merging)
##### 📜 Description: Merge Sort divides the array into halves, recursively sorts each half, and them merges the sorted halves to produce the final Sorted array.

##### 🛠️ 🗜️ Implementation
    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge  the two sorted halves into a single sorted array

##### ⏳ ⏰ Time Complexity
    - Best Case: 0(n log n)
    - Average Case: 0(n log n)
    - Worst Case: 0(n log n)


### 6. HEAP SORT

##### 📌 Technique: Selection Based
##### 📐 Stability: No (Does Not Preserve the relative order of equal elements)
##### ☢️ Recursive: Can be implemented both recursively and iteratively.
##### 💾 In-place: Yes 
##### 📜 Description: Heap Sort builds a max-heap(or min-heap) from the input data and repeatedly extracts the minimum(or maximum) element from the heap and rebuilds the heap until the data is sorted.

##### 🛠️ 🗜️ IMplementation
    1. Build a max-heap from the input data.
    2. Swap the first element(maximum) with the last element.
    3. Reduce the heap size by one and heapify the root element to maintain the heap property.
    4. Repeat steps 2 - 3 until heap is empty.

##### ⏳ ⏰ Time Complexity
- Best Case: 0(n log n)
- Average Case: 0(n log n)
- Worst Case: 0(n log n)