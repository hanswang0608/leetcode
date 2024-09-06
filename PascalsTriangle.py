class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            prev = rows[-1]
            rows.append([1])
            for j in range(1, len(prev)):
                rows[-1].append(prev[j-1] + prev[j])
            rows[-1].append(1)
        return rows