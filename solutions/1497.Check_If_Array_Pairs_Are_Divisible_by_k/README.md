## 1497. Check If Array Pairs Are Divisible by k

### Problem Link 
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

### Note
This problem seems to have no way to start. But when look into deeper, there's interested finding.

```
a = m * k + mod_a
b = n * k + mod_b
# If a + b is divisible by k
a + b = (m + n) * k + (mod_a + mod_b) 
mod_a + mod_b = 0 or k
```

So we can do `mod` for entire `arr`, the problem now is to check `count(i) == count(k - i) for i in range(k)`. 
If all pair counts are equal, then `arr` is divisible by `k`.