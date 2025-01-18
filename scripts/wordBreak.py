class Solution:

    def wordBreak(self, wordList, string):
        strlen = len(string)
        if strlen == 0:
            return True
        
        for i in range(1, strlen+1):
            prefix = string[:i]
            postFix = string[i:]

            if prefix in wordList and self.wordBreak(wordList, postFix):
                return True
        
        return False


wordList = ["mobile", "samsung", "sam", "sung", "man",
                "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream"]

print(Solution().wordBreak(wordList, "ilikesamsung"))