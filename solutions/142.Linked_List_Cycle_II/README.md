## 142. Linked List Cycle II

### Problem Link 
https://leetcode.com/problems/linked-list-cycle-ii/

### Note
If using Hash Set this problem is easy. Let's check the follow up.

**Follow-up:**
Can you solve it without using extra space?

In problem [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), the solution is to use `Two
 Pointers` to detect cycle. Here we just need to do more upon that.
 
#### Floyd's Tortoise and Hare

Floyd's algorithm is separated into two distinct phases. 

- In the first phase, it determines whether a cycle is present 
in the list. If no cycle is present, it returns null immediately, as it is impossible to find the entrance to a 
nonexistant cycle. 
- Otherwise, it uses the located "intersection node" to find the entrance to the cycle.
 
![alt text](https://leetcode.com/problems/linked-list-cycle-ii/Figures/142/diagram.png)
 
From the graph, we can list out Formula:

```
2 * distance(tortoise) = distance(hare)
2(F + a) = F + a + b + a
2F + 2a = F + 2a + b
F = b
```

Because `F = b`, pointers starting at nodes `h` and `-F` will traverse the same number of nodes before meeting.

The meeting point is the **cycle entrance**.