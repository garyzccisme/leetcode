## 1488. Avoid Flood in The City

### Problem Link 
https://leetcode.com/problems/avoid-flood-in-the-city/

### Note
This problem seems pretty complex, however when we divide them into small cases it will become much clearer.

- When raining
    - Need to check if there is flood, so we need a `full` set to store all full lakes.
    - The `ans` must append with -1.
- When not raining
    - Now we can dry full lake. How? 
    - We have to need a `dry` to store the dry plan for lakes. How to make the dry plan?
    - It's actually a greedy algorithm: **dry the full lake with earliest next rain first**. Thus the `dry` should be a
     `Heap` so that the first one is always the earliest.
    - If we don't have a dry plan, then `ans` can append whatever.
    
Back to the first, we need an extra `lakes`(`dict[deque]`) to store the rain order for each lake. When it rains to a
 lake, we need to check if there's next rain for it, so that store the next rain date(index) to `dry`.
    
    
    