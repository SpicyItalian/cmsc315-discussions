# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.



## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

### My Reflection

I learned how a binary search tree used ordering to organize values and
reduce the work needed for a search. My insertion method placed smaller
values in the left subtree and larger values in the right subtree. The
search method used the same comparisons to choose one branch at a time.

The part that required the most care was returning the updated node from
the recursive insertion helper. This connected new children correctly and
allowed the first insertion to establish the root. I also used `None` as a
base case so searches and traversals stopped safely at empty subtrees.

I tested missing values, an empty tree, a single-node tree, and duplicate
insertions. My inventory example stored product IDs and displayed them in
sorted order through in-order traversal.

Compared with scanning an unsorted list, a balanced BST could find values
with fewer comparisons. However, inserting values in sorted order created
a chain in my implementation, making search O(n). This showed me that BST
efficiency depended on its shape, and that using a tree alone did not
guarantee logarithmic search time.
