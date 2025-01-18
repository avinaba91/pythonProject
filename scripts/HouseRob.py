from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {0:1, 1:max(nums[0], nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i-1), helper(i-2) + nums[i])
                return memo[i]
            
        return helper(n-1)


nums = [0]    
print(Solution().rob(nums))