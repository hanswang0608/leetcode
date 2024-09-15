class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(list(allowed))
        ans = 0
        for word in words:
            valid = True
            for c in word:
                if c not in allowedSet:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans