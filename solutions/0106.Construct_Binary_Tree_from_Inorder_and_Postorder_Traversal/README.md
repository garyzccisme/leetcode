## 106. Construct Binary Tree from Inorder and Postorder Traversal

### Problem Link 
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

### Note
Before starting, we need to figure out what are `Tree Depth First Traversals (Inorder, Preorder and Postorder)`.
![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
- `Inorder`(Left, Root, Right): 4 2 5 1 3
- `Preorder` (Root, Left, Right) : 1 2 4 5 3
- `Postorder` (Left, Right, Root) : 4 5 2 3 1

Given the `Postorder`, we can easily get the root value which is the last element of `Postorder`. Since there's no
 duplicated node values, we can find the index of root in `Inorder`. Thus we can get `Left_Inorder` & `Right_Inorder`.
 Finally the problem can be solve by recursion.
 
Note: finding root index in `Inorder` can be optimized by `Hash Map`.
