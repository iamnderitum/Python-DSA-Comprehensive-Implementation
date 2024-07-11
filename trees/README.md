### TREES DATA STRUCTURES

#### Overview.
###### 📌 Tree
    - A hierarchical data structure consisting of nodes, with a single node called the
      root from which zero or more child nodes descend. Each child node can have its
      own children forming a tree structure.

###### 📌 Node. 
    - An element of a tree that combines a value or data and references to its children

###### 📌 Edge
    - A connection  between two nodes.

###### 📌  Root
    - The topmost node in a tree.

###### 📌 Leaf
    - A node with no children.

###### 📌 Parent
    - A node that has one or more child nodes.

###### 📌 Child
    - A node that descends from another node.

###### 📌 Subtree
    - A tree formed by a node and its descendants.


#### Types of Trees
###### 1. 🎋 Binary Tree:
    - Each node has at most two children(Left and right).
    - Common types include full, complete, and perfect trees.

###### 2. 🎋 Binary Search Tree(BST):
    - A binary tree where each node's left subtree contains only nodes with values less than
      the node's value, and the right subtree contains only nodes with values greater than
      the node's value.


###### 3. 🎋 Balanced Trees:
    - **AVL Tree** : A self-balancing BST where the difference in heights between left & right
     subtrees is at most 1.

    - *Red-Black Tree* : A self-balancing BST with an additional property of coloring nodes red or
      black to ensure balanced height.

###### 4. 🎋 Heap:
    - A complete binary tree where each parent node is greater than or equal to (max-heap) or
      less than or equal to (min-heap) its children.

###### 5. 🎋 B-Tree:
    - A self-balancing  tree data structure that maintains sorted data and allows searches,
      sequential access, insertions, and deletions in logarithmic time. Commonly used in
      databases and file systems.

###### 6. 🎋 Trie:
    - A tree used to store a dynamic set of strings where the keys are usually strings. Used for fast retrieval.

###### 7. 🎋 N-arry Tree:
    - A tree in which each node can have at m ost N children.


#### Properties
    - Height: The length of the longest path from the root to a a leaf.
    - Depth: The length of the path from  the root to a given node.
    - Degree: The number of children a node has.
    - Balanced Tree: A tree where the height difference between  subtrees of any node is bounded.
    - FUll Tree: A tree where every node other than the leaves has two children.
    - Complete Tree: A tree where all levels except possibly  the last are fully filled
      and all nodes are as far left as possible.