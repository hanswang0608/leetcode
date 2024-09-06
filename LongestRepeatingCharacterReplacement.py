class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # optimization:
        # O(n) instead of O(26n)
        # when shrinking left, don't update majorityChar
        # works because we want to maximize length, and shrinking counter[majorityChar] will never maximize it
        # so we greedily/optimistically keep majorityChar as the most frequent ever
        # counter = defaultdict(int)
        # l = 0
        # majorityChar = s[0]
        # for r in range(len(s)):
        #     counter[s[r]] += 1
        #     if counter[s[r]] > counter[majorityChar]:
        #         majorityChar = s[r]
        #     if (r - l + 1) - counter[majorityChar] > k:
        #         counter[s[l]] -= 1
        #         l += 1
        # return (r - l + 1)

        counter = defaultdict(int)
        l = 0
        majorityFreq = 0
        longest = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            if counter[s[r]] > majorityFreq:
                majorityFreq = counter[s[r]]
            while (r - l + 1) - majorityFreq > k:
                counter[s[l]] -= 1
                l += 1
                majorityFreq = max(counter.values())
            longest = max(longest, (r - l + 1))
        return longest

# brute force O(n^3) -> check every substring
# sliding window O(26n) -> keep dict for character frequencies, window is valid if # of minority chars <= k
#   need to scan counter when shrinking left to find new majority character frequency

# "ABB"
# "AAACC"
# "ABBAAABA"