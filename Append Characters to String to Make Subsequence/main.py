class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ptr = 0
        for i in range(len(s)):
            if (s[i] == t[t_ptr]):
                t_ptr += 1
            if t_ptr == len(t):
                break
        return len(t) - t_ptr