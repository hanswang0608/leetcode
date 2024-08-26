class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += chr(len(s))
            output += s
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            size = ord(s[i])
            i += 1
            output.append(s[i:i+size])
            i += size
        return output