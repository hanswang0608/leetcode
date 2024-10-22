class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path, seen, total):
            if total == target:
                ans.append(path.copy())
                return
            if total > target or i == len(candidates):
                return
            if seen[candidates[i]] == 0:
                path.append(candidates[i])
                backtrack(i+1, path, seen, total+candidates[i])
                path.pop()
            seen[candidates[i]] += 1
            backtrack(i+1, path, seen, total)
            seen[candidates[i]] -= 1
        
        backtrack(0, [], defaultdict(int), 0)

        return ans