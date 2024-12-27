class Solution:
    def minDistanceMemoization(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # base cases
            if (i, j) == (len(word1), len(word2)):  # both reach end, 0 distance
                return 0
            if i == len(word1):                     # w2 longer, need len(word2) - j inserts
                return len(word2) - j
            if j == len(word2):                     # w1 longer, need len(word1) - i deletes
                return len(word1) - i
            

            # recurrence relations

            # matching char
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            # 3 operations
            replace = 1 + dfs(i+1, j+1)
            delete = 1 + dfs(i+1, j)
            insert = 1 + dfs(i, j+1)

            cache[(i, j)] = min(replace, delete, insert)
            return cache[(i, j)]

        return dfs(0, 0)

    # O(n^2) space tabulation
    def minDistanceTabulation(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        # initializing base cases values
        for i in range(l1+1):
            for j in range(l2+1):
                if (i, j) == (l1, l2):
                    dp[i][j] = 0
                elif j == l2:
                    dp[i][j] = l1 - i
                elif i == l1:
                    dp[i][j] = l2 - j
        
        # bottom-up tabulation
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    replace = 1 + dp[i+1][j+1]
                    delete = 1 + dp[i+1][j]
                    insert = 1 + dp[i][j+1]
                    dp[i][j] = min(replace, delete, insert)
        return dp[0][0]

    # optimizied O(n) space
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        # dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        dp = [0 for _ in range(l2+1)]

        # initialize base cases
        for j in range(l2):
            dp[j] = l2 - j
        
        # bottom-up tabulation
        for i in range(l1-1, -1, -1):
            newDp = [0 for _ in range(l2+1)]
            newDp[l2] = l1 - i
            for j in range(l2-1, -1, -1):
                if word1[i] == word2[j]:
                    # dp[i][j] = dp[i+1][j+1]
                    newDp[j] = dp[j+1]
                else:
                    # replace = 1 + dp[i+1][j+1]
                    # delete = 1 + dp[i+1][j]
                    # insert = 1 + dp[i][j+1]
                    # dp[i][j] = min(replace, delete, insert)
                    replace = 1 + dp[j+1]
                    delete = 1 + dp[j]
                    insert = 1 + newDp[j+1]
                    newDp[j] = min(replace, delete, insert)
            dp = newDp
        # return dp[0][0]
        return dp[0]

# 5:15

# finding levenshtein distance

# l1 = len(word1), l2 = len(word2)
# base cases:
# dp[l1][l2] = 0 -> "" and "" have distance of 0
# dp[i][l2] = l1 - i    word1 is longer than word2, need l1-i deletes to match
# dp[l1][j] = l2 - j    word2 is longer than word1, need l2-j inserts to match
# dp[i][j] = distance of word1[i:] and word2[j:]

# let x = word1[i], y = word2[j]
# if x==y: dp[i][j] = dp[i+1][j+1] because they are already the same
# if x!=y: 3 choices, take minimum
#   1. replace char -> 1 + dp[i+1][j+1]
#   2. delete char -> 1 + dp[i+1][j]
#   3. insert char -> 1 + dp[i][j+1]

# "abcdefg", "abdefgh" = 2, delete(c)->insert(h)
# "abdefgh", "abcdefg" = 2, insert(c)->delete(h)
