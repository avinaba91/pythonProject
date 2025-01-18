from typing import List

class Subsets:
    def solution(Self, nums: List[int]):
        sol, sub = [], []
        length = len(nums)
        nums.sort()
        

        def backtrack(i: int, sub: List[int]):
            if i == length:
                sol.append(sub[::])
                return
            
            sub.append(nums[i])
            backtrack(i+1, sub)
            sub.pop()
            
            while i+1 < length and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, sub)
        
        backtrack(0, sub)
        
        print(sol)

nums = [1,2,2,3,3]
print(Subsets().solution(nums))