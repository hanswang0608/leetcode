class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        def backtrack(s, path):
            if not s:
                output.append(path)
            else:
                for i in range(1, len(s)+1):
                    # if the substring is a palindrome, continue dfs, otherwise discard solution and backtrack
                    if s[:i] == s[i-1::-1]:
                        backtrack(s[i:], path + [s[:i]])
        
        backtrack(s, [])

        return output