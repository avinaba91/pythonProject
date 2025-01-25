from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort() 
        res = 0
        minDiff = float('inf')

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if abs(currSum - target) < minDiff:
                    minDiff = abs(currSum - target)
                    res = currSum
                elif abs(currSum - target) == minDiff:
                    res = max(res, currSum)

                if currSum > target:
                    r -= 1
                else:
                    l += 1
        return res
        


nums = [-4,2,2,3,3,3]
target = 1

print(Solution().threeSumClosest(nums, target))