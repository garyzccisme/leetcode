## 528. Random Pick with Weight

### Problem Link 
https://leetcode.com/problems/random-pick-with-weight/

### Note
In Statistics, if we nomalize (divided by `self.cdf[-1]`) the `self.cdf` into [0, 1], it's actually a discrete distribution `cdf ` sequence. For cdf function, given `X` you can get the Cumulative Probability (aka percentile) of `X`, which is `Prob(x <= X) `.

The question is actually asking to generate random samples given by a specific statistical distribution. How?

Priciple is easy, take uniform sample from the `cdf` squence ( which can be realized by `random` ), then use `inverse_cdf` function to find the variable `X`. The binary search here is actually `inverse_cdf` function, that returns the `X` given by a Cumulative Probability.


After you take enough samples by this way, and plot the histogram of these samples, you will found the plot fits well for the given distribution.


- More information and proof can be found in [Wikipedia](https://en.wikipedia.org/wiki/Inverse_transform_sampling) & [StackExchange](https://stats.stackexchange.com/questions/161635/why-is-the-cdf-of-a-sample-uniformly-distributed).
