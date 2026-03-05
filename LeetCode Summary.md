# LeetCode 刷题常用思路与模板总结

## 1. Array / String

**主要思路：**
- 遍历、双指针、滑动窗口、前缀和、计数、排序
- 注意边界和原地操作

**常用模板：**
- 遍历：`for i in range(len(nums))`
- 双指针：`left, right = 0, 0`
- 滑动窗口：`while right < n: ...`
- 排序：`nums.sort()`

**典型题型：**
- Remove Duplicates/Element（双指针）
- Rotate Array（环状处理、反转）
- Product of Array Except Self（前后缀积）
- Trapping Rain Water（双指针/单调栈）

**时间复杂度：**
- 遍历 O(n)
- 排序 O(n log n)
- 滑动窗口 O(n)

---

## 2. Two Pointers / Sliding Window

**主要思路：**
- 两个指针维护区间，动态调整窗口
- 适合子数组/子串问题

**模板：**
```python
left = 0
for right in range(len(nums)):
    # 扩展窗口
    while 不满足条件:
        # 缩小窗口
        left += 1
```

**典型题型：**
- Valid Palindrome
- Longest Substring Without Repeating Characters
- Minimum Window Substring

**时间复杂度：** O(n)

---

## 3. Matrix

**主要思路：**
- 按行按列遍历，方向数组
- 处理边界和访问标记

**模板：**
```python
for i in range(m):
    for j in range(n):
        # 处理 grid[i][j]
```

```python
# Check boundary for (i, j)
for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
    if 0 <= x < m and 0 <= y < n:
        dfs(x, y, ...)
```

**典型题型：**
- Spiral Matrix
- Rotate Image（原地旋转）
- Set Matrix Zeroes

---

## 4. Hashmap

**主要思路：**
- 统计频率、映射关系、查重
- 用 dict 或 set

**典型题型：**
- Two Sum
- Group Anagrams
- Valid Anagram

---

## 5. Intervals

**主要思路：**
- 排序后合并/插入/扫描
- 关注区间重叠和边界

**典型题型：**
- Merge Intervals
- Insert Interval

---

## 6. Stack

**主要思路：**
- 括号匹配、逆序处理、单调栈
- 适合需要回退的场景

**模板：**
```python
stack = []
for x in arr:
    while stack and 条件:
        stack.pop()
    stack.append(x)
```

**典型题型：**
- Valid Parentheses
- Min Stack
- Trapping Rain Water（单调栈）

---

## 7. Linked List

**主要思路：**
- 快慢指针、反转、合并、分割
- 注意 dummy 节点和边界

**模板：**
```python
dummy = ListNode(0)
cur = dummy
while head:
    # 操作
    head = head.next
return dummy.next
```

**典型题型：**
- Merge Two Sorted Lists
- Reverse Linked List
- Remove Nth Node From End of List

---

## 8. Binary Tree / BST

**主要思路：**
- 递归（前中后序）、BFS/DFS、分治
- BST 特性：左小右大

**模板：**
- 递归遍历：
```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    # 处理
    dfs(node.right)
```

- BFS：
```python
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    # 处理
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

**典型题型：**
- Maximum Depth of Binary Tree
- Lowest Common Ancestor
- Validate BST

---

## 9. Graph

**主要思路：**
- BFS/DFS 遍历、并查集、拓扑排序
- 适合连通性、最短路径、环检测

**模板：**
- BFS/DFS 同树
- 拓扑排序：
```python
from collections import deque
queue = deque([入度为0的节点])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        # 更新入度
```

**典型题型：**
- Number of Islands
- Clone Graph
- Course Schedule

---

## 10. Trie

**主要思路：**
- 字典树，适合前缀查找、字符串集合

**模板：**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

---

## 11. Backtracking

**主要思路：**
- 递归枚举所有可能，遇到不合法就回溯
- 适合组合、排列、子集、N皇后

**模板：**
```python
def backtrack(path, choices):
    if meet_condition:
        res.append(path)
        return
    for choice in choices:
        mark_choice
        backtrack(path + [choice], new_choices)
        undo_mark
```

**典型题型：**
- Permutations
- Combination Sum
- N-Queens

---

## 12. Divide & Conquer

**主要思路：**
- 分成子问题递归解决，合并结果
- 适合归并、树、排序、区间问题

**模板：**
```python
def helper(l, r):
    if l == r:
        return ...
    mid = (l + r) // 2
    left = helper(l, mid)
    right = helper(mid+1, r)
    return 合并(left, right)
```

**典型题型：**
- Merge k Sorted Lists
- Sort List
- Construct Quad Tree

---

## 13. Kadane's Algorithm

**主要思路：**
- 连续子数组最大和，动态维护当前和和最大和

**模板：**
```python
cur_sum = max_sum = nums[0]
for num in nums[1:]:
    cur_sum = max(num, cur_sum + num)
    max_sum = max(max_sum, cur_sum)
```

---

## 14. Binary Search

**主要思路：**
- 有序数组/区间查找，O(log n)
- 变种：找插入点、左/右边界、峰值等

**模板（你记住的）：**
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return left  # 插入点
```

---

## 15. Heap

**主要思路：**
- 维护一组最大/最小元素，优先队列
- 适合 Top K、动态中位数

**模板：**
```python
import heapq
heapq.heappush(heap, x)
heapq.heappop(heap)
```

**典型题型：**
- Kth Largest Element
- Find Median from Data Stream

---

## 16. Bit Manipulation

**主要思路：**
- 位运算（&, |, ^, ~, <<, >>），适合状态压缩、集合、计数
- 常见技巧：异或找唯一数、lowbit、mask

**模板：**
```python
# 统计1的个数
count = 0
while n:
    n &= n - 1
    count += 1
```

---

## 17. Math

**主要思路：**
- 模拟、整除、取余、质数、位操作
- 适合数字处理、进制转换

---

## 18. Dynamic Programming

**主要思路：**
- 明确状态、转移方程、初始条件
- 1D/2D DP，背包、区间、子序列、路径计数

**模板（自底向上）：**
```python
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = ...
return dp[n]
```

**模板（自顶向下）：**
```python
@lru_cache(None)
def dfs(i):
    if i == 0: return ...
    return min(dfs(i-1), dfs(i-2)) + ...
```

**典型题型：**
- Climbing Stairs
- House Robber
- Longest Increasing Subsequence
- Edit Distance

---

## tag 识别与时间复杂度

- **数组/字符串遍历**：O(n)
- **排序/归并/堆**：O(n log n)
- **二分查找**：O(log n)
- **哈希表/集合**：O(1) 查找/插入
- **滑动窗口/双指针**：O(n)
- **树/图遍历**：O(n) 或 O(V+E)
- **动态规划**：O(n)、O(n²)、O(n³)（看状态数）
- **回溯/DFS**：O(2ⁿ)、O(n!)（组合/排列）

**如何识别 tag：**
- 子数组/子串最大/最小/和/长度：滑动窗口、前缀和、Kadane
- 有序数组/区间查找：二分查找
- 频率统计、查重：哈希表
- 区间合并：排序+扫描
- 组合/排列/子集：回溯
- 路径计数、最优解：动态规划
- 连通性、最短路径：BFS/DFS/并查集
- Top K/动态中位数：堆
- 状态压缩/集合问题：位运算

---

**建议：**
- 刷题时多总结模板，遇到新题先判断属于哪个 tag，再套模板。
- 面试时先说思路，再写代码，优先用你熟悉的模板。
