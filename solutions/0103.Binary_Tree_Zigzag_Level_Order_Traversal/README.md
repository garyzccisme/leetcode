## 103. Binary Tree Zigzag Level Order Traversal

### Problem Link 
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Note
This problem is a follow up of [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/).
The only difference is all even levels are in reversed order, assuming `root` is on 1st level.

Clearly, we can use `DFS` & `BFS` to do simple order traversal and then reverse even levels.

There're two more efficient ways to get the answer when traversing.

#### 1. BFS with stack

- When traversing current level nodes `cur_level`, we not only record the `node.val` but also add next level nodes 
`next_level` into queue. 
- When start to traverse `next_level`, the order is reversed, which is the **last in first out (LIFO)**. 

This problem can be solve by using `stack`, where you append and pop elements by LIFO.

#### 2. DFS
Implementing `DFS` method is easier. Just need to add extra `level` parameter into `dfs` function to distinguish 
`insert` and `append`.

