class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if (haystack[i] == needle[0]):
                found = True
                for j in range(len(needle)):
                    if i+j >= len(haystack):
                        return -1
                    if haystack[i+j] != needle[j]:
                        found = False
                        break
                if found:
                    return i
        return -1
                