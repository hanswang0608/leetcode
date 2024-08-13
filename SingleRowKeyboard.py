class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyToIndex = {}
        for i, key in enumerate(keyboard):
            keyToIndex[key] = i
        
        prevKeyIndex = 0
        time = 0
        for c in word:
            time += abs(keyToIndex[c] - prevKeyIndex)
            prevKeyIndex = keyToIndex[c]
        
        return time