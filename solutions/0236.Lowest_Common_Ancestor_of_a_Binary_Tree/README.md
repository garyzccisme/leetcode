## 236. Lowest Common Ancestor of a Binary Tree

### Problem Link 
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

### Note
First the given nodes `p` and `q` are to be searched in a binary tree and then their lowest common ancestor is to be
 found. We can resort to a normal tree traversal to search for the two nodes. Once we reach the desired nodes `p` and `q`, 
 we can backtrack and find the lowest common ancestor.
![alt text](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/Figures/236/236_LCA_Binary_1.png)

- The brute force solution is to search both nodes separately and compare paths.
- Better way is to find both nodes in one search. 