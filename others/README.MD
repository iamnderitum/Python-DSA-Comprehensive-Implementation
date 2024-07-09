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

## Dictionaries
#### Overview:
- Dictionaries in python are unordered collections of items.
- Each item in a dictionary is a key-pair value.
- Dictionaries are mutable.
- Dictionaries are indexed by keys, which can be of any immutable type(e.g., strings, numbers, tuples)

#### Creating Dictionaries:
- Dictionaries can be created using curly braces "{}" with key-pairs, or using the "dict()" constructor.
  ~~~
  # Using curly braces
  my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
  }

  # Using dict() constructor
  my_dict = dict(name="Alice", age=25, city="New York")
  ~~~

#### Accessing Values.
  - Values are accessed using their keys.
  ~~~
  print(my_dict["name"])
  ~~~
  - Accessing a non-existent key raises a KeyError
  - Use the get() method to safely access values with a default return value
  ~~~
  print(my_dict.get("country", "Unknown"))  # Output: Unknown
  ~~~

#### Adding and Modifying Entries
 - Add a new key-value pair or update the value of an existing key by assigning a value to the key.
  ~~~
  my_dict["email"] = "alice@example.com"  # Adding
  my_dict["age"] = 26  # Modifying
  ~~~
#### Removing Entries
- Use "del" statement or pop() method to remove items.
  ~~~
  del my_dict["city"]  # Using del statement

  email = my_dict.pop("email")  # Using pop() method, returns the value
  ~~~
- Use "popitem()" to remove and return the last inserted key-pair value.
- Use "clear" to remove all items from the dictionary.


##### Note that we cannot change/modify a dictionary while Iterating over it. Instead, Identify the key, then remove it.

### Dictionary Methods:
    - keys() - Returns a view object of all keys in the dictionary.
    - values() - Returns a view object of all values in the dictionary.
    - items() - Returns a view Object of all key-value pairs in the dictionary.
    - update() - Updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
    - setdefault() - Returns the value of a key if it is in the dictionary; if not, inserts the key with a specified value.

### Dictionaly Comprehensions
- Create dictionaries using a syntax similar to list comprehensions.
  ~~~
  squares = {x: x*x for x in range(6)}
  # squares is {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  ~~~


### Iterating Over Dictionaries
- Iterate over keys, values, or key-value pairs.
  ~~~
  for key in my_dict:
    print(key)  # Iterate over keys

  for value in my_dict.values():
    print(value)  # Iterate over values

  for key, value in my_dict.items():
    print(key, value)  # Iterate over key-value pairs
  ~~~

### Dictionary Characteristics
- Unordered - As of Python 3.7, dictionaries maintain insertion order as an implementation detail. From Python 3.8 onwards, this became a language feature.
- Keys Must Be Immutable: Keys must be of an immutable type(eg. strings, numbers, tuples)
- Keys Must Be Unique - Assigning a new value to an existing key will overwrite the old value.

### Common Use Cases
##### Mapping
- Associating keys with values, like an address book where names are keys and addresses are values.

##### Counters
- Counting occurances of items, such as counting the frequency of words in a text.

##### Grouping
- Grouping items by a common keys, like organizing a list of students by their grades.