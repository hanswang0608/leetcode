class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1Freq = Counter(s1)
        s2Freq = defaultdict(int)
        
        for r, c in enumerate(s2):
            s2Freq[c] += 1
            while s2Freq[c] > s1Freq[c]:
                s2Freq[s2[l]] -= 1
                l += 1
            if (r - l + 1) == len(s1):
                return True
        
        return False

# brute force O(n^3) -> for every n^2 substrings in s2, compare character frequencies
# sliding window O(n) -> keep dictionary of frequencies for window, grow while freqs of s2 < s1, shrink otherwise