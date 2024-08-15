class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()
        temp = []
        for i in range(len(s), 0, -k):
            start = max(i-k, 0)
            temp.append(s[start:i])
        return '-'.join(reversed(temp))