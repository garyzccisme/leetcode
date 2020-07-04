## 212. Word Search II

### Problem Link 
https://leetcode.com/problems/word-search-ii/

### Note
This problem is a harder follow up of [79. Word Search](https://leetcode.com/problems/word-search/). Simply using
 `DFS` will cause time limit exceeded. This problem combines both `DFS` and `Trie`.
 
The overall workflow of the algorithm is intuitive, which consists of a loop over each cell in the board and a recursive 
function call starting from the cell. Here is the skeleton of the algorithm.
- We build a Trie out of the words in the dictionary, which would be used for the matching process later.
- Starting from each cell, we start the `DFS` exploration, if there exists any word in the dictionary that starts with 
the letter in the cell.
- Inside the `DFS`, we explore the neighbor cells around the current cell for the next recursive call. At each call, 
we check if the sequence of letters that we traverse so far matches any word in the dictionary, with the help of the 
Trie data structure that we built at the beginning.

#### Optimizations

- Backtrack along the nodes in Trie.
    - One could use Trie simply as a dictionary to quickly find the match of words and prefixes, i.e. at each step of 
    backtracking, we start all over from the root of the Trie. This could work.
    - However, a more efficient way would be to traverse the Trie together with the progress of backtracking, i.e. at 
    each step of backtracking(TrieNode), the depth of the TrieNode corresponds to the length of the prefix that we've 
    matched so far. 
- Gradually **prune** the nodes in Trie during the backtracking.
    - The idea is motivated by the fact that the time complexity of the overall algorithm sort of depends on the size 
    of the Trie. For a leaf node in Trie, once we traverse it (i.e. find a matched word), we would no longer need to 
    traverse it again. As a result, we could prune it out from the Trie.
    - Gradually, those non-leaf nodes could become leaf nodes later, since we trim their children leaf nodes. In the 
    extreme case, the Trie would become empty, once we find a match for all the words in the dictionary.
    ![alt text](https://leetcode.com/problems/word-search-ii/Figures/212/212_trie_prune.png)
- Keep words in the Trie.
    - One might use a flag in the Trie node to indicate if the path to the current code match any word in the dictionary. 
    It is not necessary to keep the words in the Trie.
    - However, doing so could improve the performance of the algorithm a bit. One benefit is that one would not need
    to pass the prefix as the parameter in the backtracking() call. And this could speed up a bit the recursive call. 
    Similarly, one does not need to reconstruct the matched word from the prefix, if we keep the words in Trie.
- Remove the matched words from the Trie.
    - In the problem, we are asked to return all the matched words, rather than the number of potential matches. 
    Therefore, once we reach certain Trie node that contains a match of word, we could simply remove the match from the Trie.
    - As a side benefit, we do not need to check if there is any duplicate in the result set. As a result, we could
     simply use a list instead of set to keep the results, which could speed up the solution a bit.