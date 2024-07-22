class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        heights.sort(reverse=True)
        output = []
        for h in heights:
            output.append(dic[h])
        return output