## 662. Maximum Width of Binary Tree

### Problem Link 
https://leetcode.com/problems/maximum-width-of-binary-tree/

### Note
The key of this problem is how to count nodes by index. 

In [314. Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/), 
the index is designed by giving `left child` with `index - 1` and `right child` with `index + 1`:
```
	    0
	  -1, 1
       -2, 0, 0, 2
-3, -1, -1, 1, -1, 1, 1, 3
```
However, in this problem we can't design index by this since there're duplicate indexes in same level and we can't 
determine the number of nodes. We need unique index for every node in same level:
```
          1
         1, 2
      1, 2, 3, 4
1, 2, 3, 4, 5, 6, 7, 8
```
Thus for each `node` with `index`:
- `index(node.left) = index(node) * 2 - 1` 
- `index(node.right) = index(node) * 2 `

After we figure out this, it's not hard to implement both `BFS` & `DFS` code.