from typing import List

class Solution(object):
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0 , len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1]

instance = Solution()
print(instance.twoSum([2,7,11,15], 26)) # returns [1,2]