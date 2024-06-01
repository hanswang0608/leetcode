class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedlist = sorted(score, reverse=True)
        m = {}
        for i in range(len(sortedlist)):
            if (i == 0):
                m[sortedlist[i]] = "Gold Medal"
            elif (i == 1):
                m[sortedlist[i]] = "Silver Medal"
            elif (i == 2):
                m[sortedlist[i]] = "Bronze Medal"
            else:
                m[sortedlist[i]] = str(i + 1)

        for i in range(len(score)):
            score[i] = m[score[i]]
        
        return score