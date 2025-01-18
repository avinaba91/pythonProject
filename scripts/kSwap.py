class Solution:
    
    def setdigit(self, curr, index, k, res):
        # Function to keep the maximum result
        def match(curr, res):
            # If current number is larger, update result
            if curr > res:
                res = curr
            return res
    
        def swap(i, j, num):
            s = list(num)
            s[i], s[j] = s[j], s[i]
            num = "".join(s)
            return num

        n = len(curr)
        
        if k == 0 or index == n-1:
            return match(curr, res)
        
        maxNum = -1

        for i in range(index, n):
            maxNum = max(int(curr[i]), maxNum)
        print(maxNum)
        print(curr[index])
        if curr[index] == maxNum:
            res = self.setdigit(curr, index+1, k, res)
            return res
        
        for i in range(index+1, n):
            if maxNum == int(curr[i]):
                print(i)
                curr = swap(index, i, curr)
                print(curr)
                res = self.setdigit(curr, index+1, k-1, res)
                curr = swap(index, i, curr)

        return res

k = 2
s = "228899"
print(Solution().setdigit(s, 0, k, s))
        

        
