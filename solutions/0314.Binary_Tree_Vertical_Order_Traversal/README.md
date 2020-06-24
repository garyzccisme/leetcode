## 314. Binary Tree Vertical Order Traversal

### Problem Link 
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

### Note
This problem is a follow up of [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/).
We can use both `BFS` & `DFS` to solve. 

- `DFS`

    For each list in the answer the node's values are ordered by their node level. Using `DFS` is not very
     efficient here, since we need to save both column index and level number, then do sorting.

- `BFS`
    
    The best way is to use a `dict` to save the column index then list by order. Also note that the column indexes are
     continuous so we only need to get min & max column index in stead of sorting. The time complexity can be reduced
      from `O(N*log(N))` to `O(N)`.
 
 