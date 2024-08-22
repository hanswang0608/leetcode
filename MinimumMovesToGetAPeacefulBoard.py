class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        rooks.sort(key=lambda x: x[0])

        moves = 0
        for i in range(len(rooks)):
            moves += abs(rooks[i][0] - i)

        rooks.sort(key=lambda x: x[1])
        for i in range(len(rooks)):
            moves += abs(rooks[i][1] - i)

        return moves