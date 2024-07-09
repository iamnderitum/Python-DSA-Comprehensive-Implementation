## Lists & Tuples

### Overview
- Lists and tuples are data structures in Python used to store collections of items.
- Lists are mutable, meaning their elements can be changed after creation.
- Tuples are immutable, meaning once created, their elements cannot be changed

### Homogeneous vs. Heterogeneous
- ##### Homogeneous : All elements are of the same type
- ##### Heterogeneous: Elements can be of different types

### List Methods(Mutable)
- Lists have several methods to them due to their mutable nature:
  - append(item) - Adds an item to the end of the list.
  - extend(iterable) - Extends a list by appending elements from an iterable.
  - insert(index, item) - Inserts an item at a given position.
  - remove(item) - Removes the first occurance of an item.
  - pop([index]) - Removes and returns the item at the given position(default is the last item)
  - clear() - Removes all items from the list.
  - sort() - Sorts the list in ascending order.
  - reverse() - Reverses the elements of the list in place.
  - copy() - Returns a shallow copy of the list.

### Tuple Methods(Immutable)
- Tuple have fewer methods since they cannot be modified after creation:
    - count(item) - Returns the number of times an item appears in the tuple.
    - index(item) - Returns the index of the first occurance of an item.

### Methods available for both Lists & Tuples
- Length (len()) - Returns the number of items in the list or tuple.
- Membership("in") - Checks if an item is in the list or tuple
    ~~~
    2 in [1, 2, 3]   # Returns True
    4 in (1, 2, 3)   # Returns False
    ~~~
- Concatenation("+") - Combines two lists or tuples
  ~~~
  [1, 2] + [3, 4]    # Returns [1, 2, 3, 4]
  (1, 2) + (3, 4)    # Returns (1, 2, 3, 4)
  ~~~

- Repetation("*") - Repeats the list or tuple a given number of times.
  ~~~
  [1, 2] + [3, 4]    # Returns [1, 2, 3, 4]
  (1, 2) + (3, 4)    # Returns (1, 2, 3, 4)
  ~~~

- Slicing - Accesses a range of items in the list or tuple.
  ~~~
  [1, 2, 3, 4][1:3]    # Returns [2, 3]
  (1, 2, 3, 4)[:2]     # Returns (1, 2)
  ~~~

- Count("count(item)") - Returns the number of times an item appears in the list or tuple.
  ~~~
  my_list = [1, 2, 2, 3]
  my_list.count(2)
  # Returns 2

  my_tuple = (1, 2, 2, 3)
  my_tuple.count(2)
  # Returns 2
  ~~~

- Index ("index(item)") - Returns the index of the first occurance of an item
  ~~~
  my_list = [1, 2, 3]
  my_list.index(2)
  # Returns 1

  my_tuple = (1, 2, 3)
  my_tuple.index(2)
  # Returns 1
  ~~~

### Summary
- Lists are mutable and support a wide range of methods for modification
- Tuples are immutable and support only a few methods for querying their contents.

DSA-Comprehensive-Implementation
Data structures and algorithm Implementation, From the most basic data structures likes lists and tuples, to More complex and advanced data structures like Trees and graphs

DSA-Comprehensive-Implementation
Data structures and algorithm Implementation, From the most basic data structures likes lists and tuples, to More complex and advanced data structures like Trees and graphs