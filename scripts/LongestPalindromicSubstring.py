class Solution:
    def longestPalindrome(self, s: str) -> str:
        pickSize = 0
        palArray = []
        markedList = ""
        start,end=0,0
        
        if len(s) == 1:
            return s

        def checkPalindromic(markedList):

            listSize = len(markedList)
            arrayLen = int(listSize/2)
            for i in range(arrayLen):
                if markedList[i] == markedList[listSize-1-i]:
                    continue
                else:
                    return False
            return True
        
        
        
        
        while start < len(s)-1:
            markedList = markedList + s[end]
            strLen = end - start
            if checkPalindromic(markedList) and strLen > pickSize:
                pickSize = strLen
                palArray = markedList[::]
            end += 1

            if end == len(s):
                start += 1
                end = start 
                markedList = ""    
        return palArray

s="a"
print(Solution().longestPalindrome(s))