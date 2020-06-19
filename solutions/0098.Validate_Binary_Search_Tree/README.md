## 98. Validate Binary Search Tree

### Problem Link 
https://leetcode.com/problems/validate-binary-search-tree/

### Note
The Binary Search Tree has following properties:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Thus the problem can be solved easily by `DFS`, passing with `upper` & `lower` and checking the `node.val`.