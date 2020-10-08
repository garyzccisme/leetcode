## 1288. Remove Covered Intervals

### Problem Link 
https://leetcode.com/problems/remove-covered-intervals/

### Note
Intuitively, the problem can be solved with `O(N^2)` solution that to compare each interval with others.
However, this solution will do duplicated work. 

For example: given `intervals = [a, b, c]`, if we know `b` is in `a`, we actually don't need to compare `b` and `c`.

Here we can sort `intervals` to help us. 
- Sort ascending by interval left value.
- Sort descending by interval right value.

After the `sort`, we can find that for each interval, possible covering interval is always ordered before it.

Thus here we just need to iterate the sorted `intervals`:
- For current `interval`, check the right value with previous interval right value.
    - If `right <= pre_right`, then the current `interval` is covered.
    - Else, let `pre_right = right`. 
- Move on to next `interval`.
