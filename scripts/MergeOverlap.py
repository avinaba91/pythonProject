from typing import *

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda interval: interval[0])
        newList = []
        start = -1
        end = -1
        length = len(intervals)
        i = 0
        while i < length:
            a = intervals[i][0]
            b = intervals[i][1]

            if a > end or b < start:
                newList.append(intervals[i])
                end = b
                start = a
            
            if a < start:
                interval = newList.pop()
                interval[0] = a
                newList.append(interval)
                start = a
            
            if b > end:
                interval = newList.pop()
                interval[1] = b
                end = b
                newList.append(interval)
            
            i += 1
        return newList
    
intervals = [[1,4],[0,4]]
print(Solution().merge(intervals))
            



        