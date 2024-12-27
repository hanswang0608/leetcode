class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {
            "1":'A',
            "2":'B',
            "3":'C',
            "4":'D',
            "5":'E',
            "6":'F',
            "7":'G',
            "8":'H',
            "9":'I',
            "10":'J',
            "11":'K',
            "12":'L',
            "13":'M',
            "14":'N',
            "15":'O',
            "16":'P',
            "17":'Q',
            "18":'R',
            "19":'S',
            "20":'T',
            "21":'U',
            "22":'V',
            "23":'W',
            "24":'X',
            "25":'Y',
            "26":'Z'
        }
        prev, cur = None, 1
        # iterate from end of string to start
        for i in reversed(range(len(s))):
            temp = 0
            if s[i] in mapping:
                temp += cur
            if len(s)-i > 1 and s[i:i+2] in mapping:
                temp += prev
            prev = cur
            cur = temp
        return cur
        
# bottom-up tabulation
# iterate from end of string to start, since end of string is "bottom"
# if leftmost char can be decoded, tally subproblem with leftmost char removed
# if leftmost 2 chars can be decoded, tally subproblem with leftmost 2 chars removed
# f("") = 1 -> reaching empty string means whole string was decoded
# f(s) = (if s[0] then dp[i+1]) + (if s[0:2] then dp[i+2])

        
# can the string be empty
# is there an upper bound to the string length
# will there always be at least 1 valid decoding if the string isn't empty