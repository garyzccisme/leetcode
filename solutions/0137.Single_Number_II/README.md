## 137. Single Number II

### Problem Link 
https://leetcode.com/problems/single-number-ii/

### Note
This Problem is a follow up of [136. Single Number](https://leetcode.com/problems/single-number/).

- Hash Map & Hash Set
- Bit Manipulation. [Python Bitwise Operator](https://wiki.python.org/moin/BitwiseOperators)

#### XOR
XOR operator could be used to detect the bit which appears odd number of times: 1, 3, 5, etc.

XOR of zero and a bit results in that bit

`0 ^ x = x`

XOR of two equal bits (even if they are zeros) results in a zero

`x ^ x = 0`

and so on and so forth, i.e. one could see the bit in a bitmask only if it appears odd number of times.
![alt text](https://leetcode.com/problems/single-number-ii/Figures/137/xor.png)

#### AND and NOT
To separate number that appears once from a number that appears three times let's use two bitmasks instead of one: seen_once and seen_twice.

The idea is to

- change seen_once only if seen_twice is unchanged
- change seen_twice only if seen_once is unchanged
![alt_text](https://leetcode.com/problems/single-number-ii/Figures/137/three.png)
This way bitmask seen_once will keep only the number which appears once and not the numbers which appear three times.