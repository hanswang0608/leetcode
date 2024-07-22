class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set([(x,y) for x,y in points])
        output = float('inf')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1,y2) in points_set and (x2,y1) in points_set:
                    output = min(output, abs(x2-x1)*abs(y2-y1))
        return output if output != float('inf') else 0