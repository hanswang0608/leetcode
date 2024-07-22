class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(min(len(word1), len(word2))):
            output += word1[i]
            output += word2[i]

        if len(word1) < len(word2):
            output += word2[len(word1):]
        elif len(word2) < len(word1):
            output += word1[len(word2):]
        
        return output