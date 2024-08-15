class Solution:
    # brute force O(n^3), TLE
    # def oddEvenJumps(self, arr: List[int]) -> int:
    #     ans = 0
    #     for startingPos in range(len(arr)):
    #         i = startingPos
    #         oddJump = True
    #         # path = [arr[i]]
    #         while True:
    #             if i == len(arr)-1:
    #                 ans += 1
    #                 # print(path)
    #                 break
    #             nextJump = None
    #             for j in range(i+1, len(arr)):
    #                 if oddJump and arr[i] <= arr[j] and (nextJump is None or arr[j] < arr[nextJump]):
    #                     nextJump = j
    #                 elif not oddJump and arr[i] >= arr[j] and (nextJump is None or arr[j] > arr[nextJump]):
    #                     nextJump = j
    #             if not nextJump:
    #                 break
    #             else:
    #                 i = nextJump
    #                 oddJump = not oddJump
    #                 # path.append(arr[i])
    #     return ans

    # DP O(n^2), TLE
    # use dp to cache subproblems, but finding the next j to jump to is still expensive
    # def oddEvenJumps(self, arr: List[int]) -> int:
    #     dp = [[False]*2 for _ in range(len(arr))]
    #     dp[-1][0] = dp[-1][1] = True
    #     for i in range(len(arr)-2, -1, -1):
    #         for k in [0,1]:
    #             oddJump = k % 2 == 1
    #             # this loop to find the nextJump is O(n) and slow
    #             nextJump = None
    #             for j in range(i+1, len(arr)):
    #                 if oddJump and arr[i] <= arr[j] and (nextJump is None or arr[j] < arr[nextJump]):
    #                     nextJump = j
    #                 elif not oddJump and arr[i] >= arr[j] and (nextJump is None or arr[j] > arr[nextJump]):
    #                     nextJump = j
    #             if not nextJump:
    #                 dp[i][k] = False
    #             else:
    #                 dp[i][k] = dp[nextJump][(k+1)%2]
        
    #     ans = 0
    #     for i in range(len(arr)):
    #         if dp[i][1]:
    #             ans += 1
    #     return ans

    # DP + monotonic stack -> O(nlogn)
    # same DP process as before, but optimize the process of searching for the next j by using 2 monotonic stacks to 
    # cache the nextSmallestGreaterOrEqual indices for odd jumps, and vice versa for even jumps
    # sorting by value is needed to find next greater / smaller, so nlogn
    def oddEvenJumps(self, arr: List[int]) -> int:
        nextBigger = [0] * len(arr)
        stack = []
        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            while stack and i > stack[-1]:
                nextBigger[stack.pop()] = i
            stack.append(i)

        nextSmaller = [0] * len(arr)
        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and i > stack[-1]:
                nextSmaller[stack.pop()] = i
            stack.append(i)
        
        dp = [[False]*2 for _ in range(len(arr))]
        dp[-1][0] = dp[-1][1] = True
        for i in range(len(arr)-2, -1, -1):
            for k in [0,1]:
                oddJump = k % 2 == 1
                nextJump = None
                if oddJump:
                    nextJump = nextBigger[i]
                else:
                    nextJump = nextSmaller[i]
                if nextJump == 0:   # nextBigger[i] is 0 if there are no bigger elements after arr[i]
                    dp[i][k] = False
                else:
                    dp[i][k] = dp[nextJump][(k+1)%2]
        
        ans = 0
        for i in range(len(arr)):
            if dp[i][1]:
                ans += 1
        return ans


# brute force search from every index as a starting position -> O(n^3), 1 loop for each starting position, 1 loop to look for next jump, loop until reaching the end
# dp -> O(n^2), 1 loop from every start, 1 loop to look for next
# dp[i][j] -> if the finish can be reached from index i with j=0 (even), and j=1 (odd)
# need a way to find the next j faster to cut down from O(n^2)
# dp + monotonic stack -> O(nlogn), monotonic stack optimizes the search for j, takes nlogn to build but constant access