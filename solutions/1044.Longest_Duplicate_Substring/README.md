## 1044. Longest Duplicate Substring

### Problem Link 
https://leetcode.com/problems/longest-duplicate-substring/

### Note
This problem can be divided into two main points:

1. Perform a search by a substring length in the interval from 1 to N. -> Binary Search

    - A naive solution would be to check all possible string length one by one starting from N - 1: if there is a 
    duplicate substring of length N - 1, then of length N - 2, etc.
    - Note that if there is a duplicate substring of length k, that means that there is a duplicate substring of
    length k - 1. Hence one could use a binary search by string length here, and have the first problem solved in `O(log N)` time.

2. Check if there is a duplicate substring of a given length L. -> [Rabin-Karp's algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)

    - Can use a sliding window and save substring into Hash Map to check duplicate. However, implement a string slice
     is `O(N)`, also saving substring into hash map requires large space complexity.
    - `Rabin-Karp's algorithm` is an algorithm to find substring in a string. The main idea is to convert elements
     into numbers, thus for each sliding window it can be represented as a number. 
        - `'123' -> 123`, for next window ` '234' = 123 * 10 - 1000 + 4 = 234`, thus the check process is `O(N)`.
      