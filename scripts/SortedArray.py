from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        elif i == j:
            if target != nums[i]:
                return -1
        elif target > nums[i]:
            next = nums[i+1]
            curr = nums[i]

            while next > curr:
                if curr == target:
                    return i
                if next == target:
                    return i+1
                curr = next
                if i < j-1:
                    i += 1
                    next = nums[i+1]
                else:
                    break
        
        elif target < nums[j]:
            prev = nums[j-1]
            curr = nums[j]

            while prev < curr:
                if curr == target:
                    return j
                
                if prev == target:
                    return j-1

                curr = prev
                if j > i+1:
                    j -= 1
                    prev = nums[j-1]
                else:
                    break
        return -1
    
nums = [1,3]
target = 2
print(Solution().search(nums, target))

