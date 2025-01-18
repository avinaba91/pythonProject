from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = 0,0
        while i < n:
            if j >= m and nums1[j] == 0:
                del nums1[m]
                nums1.insert(j, nums2[i])
                i += 1
                j += 1
                m += 1
            elif nums1[j] < nums2[i]:
                j += 1
                continue
            else:
                del nums1[m]
                nums1.insert(j, nums2[i])
                m += 1
                i += 1
                j += 1



nums1,m,nums2,n = [-1,0,1,1,0,0,0,0,0], 4,[-1,0,2,2,3],5

Solution().merge(nums1, m, nums2, n)
print(nums1)