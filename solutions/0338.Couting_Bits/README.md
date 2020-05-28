## 338. Counting Bits

### Problem Link 
https://leetcode.com/problems/counting-bits/

### Note
It's not hard to find out the sequential law

0 | 1 | 1, 2 | 1, 2, 2, 3 | 1, 2, 2, 3, 2, 3, 3, 4 | ...

We divide the sequence with '|'. For each upcoming part, it's actually equal to the whole previous sequence + 1.

Start with [0]

next part is [0] + 1 = [1]

next part is [0, 1] + 1 = [1, 2]

next part is [0, 1, 1, 2] + 1 = [1, 2, 2, 3]

next part is [0, 1, 1, 2, 1, 2, 2, 3] + 1 = [1, 2, 2, 3, 2, 3, 3, 4 ]

....

**For more deep insight explanation:**
When the sequence reaches a number is 2^n (n >=0), the binary number would be started with 1 then followed by 0s. 
Without counting the first and unique 1, when the sequence keeps going, it's actually restart from 0 again. 
The number of 1's thus would be exactly the same of previous whole sequence. Now we add the heading 1 back, 
finally the new upcoming sequence would be "the whole previous sequence + 1".