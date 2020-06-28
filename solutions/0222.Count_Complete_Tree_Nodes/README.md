## 222. Count Complete Tree Nodes

### Problem Link 
https://leetcode.com/problems/count-complete-tree-nodes/

### Note
This problem could be very simple but also very worth to dive deep.

Here I listed out 3 different solutions with optimization one by one.

#### 1. O(N) Method
Use very straight forward and simple `DFS` & `BFS` to search each node in the tree. Thus don't even use any property of 
`Completed Binary Search Tree`. 

#### 2. O(N * log(N)) Method
According to the property of `Completed Binary Search Tree`, all nodes must be as left as possible, which mean as
 long as we get the height of tree and number of nodes in final level, we can compute the number of nodes:
```
# Nodes = 2 ** (# level) - 1 + # final level nodes
```
Thus we can design a `DFS` start searching from the most left, then count the `# final level nodes`. When the runner
 reaches a leaf node not in final level, then stop search. 

#### 3. O(log(N) * log(N)) Method
After we find out the rule, we can still make optimization. From previous solution, we count the `# final level nodes
` one by one, which is `O(N)` time complexity. However, using `Binary Search` can improve it to `O(log(N))`. 

Here is one little trick when implementing `Binary Search`. After we get the `left`, `right`, `mid` index, how to
 find the tree path to the correct `mid` final level node?
 
 We can convert the `mid` index into **binary format with leading zeros** to make sure the length is equal to the number
  of levels.
  
Example:

![alt text](https://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/CompleteBinary.jpg)

Check out final level, `right, left = 0, 4`. Given `mid = 2` we need to find out path to the node `J`.
- First, we convert 2 to binary adding with leading zeros: `010`.
- Consider `0` as left, `1` as right, then `010` could be `left -> right -> left`. Here is the node `J`!

After we find out the trick, it's not hard to implement the code.

