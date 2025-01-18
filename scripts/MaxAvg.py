from typing import List

class MaxAvg:
    def findMaxAvg(Self, nums: List[int], k:int) -> float:
        maxAvg = 0
        l,maxAvg, sett, length = 0,0,set(), len(nums)
        for r in range(length):
            sett.add(nums[r])
            if len(sett) == k:
                settAvg = sum(sett) / k
                maxAvg = max(settAvg, maxAvg)
                sett.remove(nums[l])
                l += 1
        return maxAvg    

#nums = [1,12,-5,-6, 50, 3]
nums = [5]
k=1
print(MaxAvg().findMaxAvg(nums, k))
