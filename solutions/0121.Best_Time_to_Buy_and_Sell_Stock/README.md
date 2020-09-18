## 121. Best Time to Buy and Sell Stock

### Problem Link 
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Note
This problem is marked as easy and the logic is very straight forward.

Here we maintain two variables `min_price` and `max_profit`. Final `max_profit` must come from one `min_price
` value.

So what we need to do is go through the `prices` and update both `min_price` & `max_profit` for each price.

Then the final `max_profit` is the result.

