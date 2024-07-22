class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        self.points[p] = self.points.get(p, 0) + 1
        print(self.points[p])

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        count = 0
        for x2, y2 in self.points:
            if x1 == x2 or abs(x1 - x2) != abs(y1 - y2):
                continue
            if (x1, y2) in self.points and (x2, y1) in self.points:
                count += self.points[(x2,y2)] * self.points[(x1,y2)] * self.points[(x2, y1)]
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)