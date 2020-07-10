## 430. Flatten a Multilevel Doubly Linked List

### Problem Link 
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

### Note
#### DFS by Recursion
Actually, if we turn the above list in 90 degrees around the clock, then suddenly a binary tree appear in front of us. 
And the flatten operation is basically what we call preorder DFS traversal (Depth-First Search).

![alt text](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/Figures/430/430_dfs_tree.png)

Now that we know the problem is basically asking us to do a preorder DFS traversal over a disguised binary tree,
 we could use this intuition to guide the implementation.

As many of you would know that there are generally two manners to implement the DFS traversal: recursion and iteration. 
We here start with the recursion, since many find it more intuitive.

Here it goes with the recursive DFS algorithm:

- First of all, we define our recursive function as `flatten_dfs(prev, curr)` which takes two pointers as input and 
returns the pointer of tail in the flattened list. The curr pointer leads to the sub-list that we would like to flatten, 
and the prev pointer points to the element that should precede the `curr` element.
- Within the recursive function `flatten_dfs(prev, curr)`, we first establish the double links between the `prev` and `curr`
nodes, as in the **preorder** DFS we take care of the **current state** first before looking into the children.
- Further in the function `flatten_dfs(prev, curr)`, we then go ahead to flatten the **left subtree** (i.e. the sublist 
pointed by the `curr.child` pointer) with the call of `flatten_dfs(curr, curr.child)`, which returns the `tail` element to 
the flattened sublist. Then with the `tail` element of the previous sublist, we then further flatten the 
**right subtree** (i.e. the sublist pointed by the `curr.next` pointer), with the call of `flatten_dfs(tail, curr.next)`.
- And voila, that is our core function. There are two additional important details that we should attend to, in order 
to obtain the correct result:
    - We should make a copy of the `curr.next` pointer before the first recursive call of `flatten_dfs(curr, curr.child)`, 
    since the `curr.next` pointer might be altered within the function.
    - After we flatten the sublist pointed by the `curr.child` pointer, we should remove the child pointer since it is
     no longer needed in the final result.
     
#### Iteration with Stack
The key is to use the data structure called stack, which is a container that follows the principle of LIFO (last in, 
first out). The element that enters the stack at last would come out first, similar with the scenario of a packed elevator.

The stack data structure helps us to construct the iteration sequence as the one created by recursion. The stack here 
mimics the behavior of the function call stack, so that we could obtain the same result without resorting to recursion.