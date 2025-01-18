class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        isword1Done,isword2Done,i,j=False,False,0,0
        updatedStr = ""
        while not (isword1Done and isword2Done):
            
            if not isword1Done:
                try:
                    updatedStr = updatedStr + word1[i]
                except Exception as ex:
                    isword1Done = True
            
            if not isword2Done:
                try:
                    updatedStr = updatedStr + word2[i]
                except Exception as ex:
                    isword2Done = True
            
            i += 1