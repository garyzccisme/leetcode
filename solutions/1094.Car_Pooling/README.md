## 1094. Car Pooling

### Problem Link 
https://leetcode.com/problems/car-pooling/

### Note
This problem can be intuitively solved with timestamp sorting by locations. Sorting time complexity is `O(Nlog(N))`.

Another way is to use bucket sort since the locations range is known. Time complexity is `O(N)`.