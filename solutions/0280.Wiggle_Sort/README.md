## 280. Wiggle Sort

### Problem Link 
https://leetcode.com/problems/wiggle-sort/

### Note
#### 1. O(N log N)
After sorting the list, we insert the tail elements (larger) back to front (smaller).

Example: 

`[1, 2, 3, 4, 5, 6, 7, 8, 9]`

We split the sorted list into two part: [1, 2, 3, 4, 5] = `head`, [6, 7, 8, 9] = `tail`. 
The logic is simply insert `tail` into gaps of each two elements in `head`.

- `[1, _, 2, _, 3, _, 4, _, 5]  <- [6, 7, 8, 9]`

The whole work flow is:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 9, 5, 6, 7, 8]
[1, 2, 3, 8, 4, 9, 5, 6, 7]
[1, 2, 7, 3, 8, 4, 9, 5, 6]
[1, 6, 2, 7, 3, 8, 4, 9, 5]
```

#### 2. O(N)
Actually, wiggle sort can be solved by one pass iteration. The logic is very intuitive:

- Compare the order of two neighbor elements.
	- If order is incorrect, then swap elements.
- Assume the index of first element is `i`, we can judge the order by odd & even.
	- If `i` is odd, then `nums[i] >= nums[i + 1]`.
	- If `i` is even, then `nums[i] <= nums[i + 1]`.

The explanation is also straight forward:
- For 3 neighbor element `a, b, c`. 
    - If `a` index is odd, the correct order should be `a >= b <= c`. After we check the order of `a` and `b`:
        -  If `b > c`, then we need to swap `b` and `c`. Since `a >= b > c` -> `a > c`, the final order `a, c, b` is correct.
    - If `a` index is even, we can aslo think in the same way. 
    - **The Swap won't change the order of previous sequence.**