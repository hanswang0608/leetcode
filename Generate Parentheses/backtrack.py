class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path, stack):
            if stack and stack[-1] == ')':
                stack.pop()
                if not stack or stack.pop() != '(':
                    return
            if len(path) == n*2:
                if not stack:
                    ans.append(''.join(path))
                return
            backtrack(path + ['('], stack + ['('])
            backtrack(path + [')'], stack + [')'])
        backtrack([], [])
        return ans