class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * (max(citations)+1)
        for citation in citations:
            counts[citation] += 1

        h_index = 0
        tally = 0
        for i in range(len(counts)-1, -1, -1):
            tally += counts[i]
            if tally >= i:
                h_index = max(h_index, i)
        return h_index