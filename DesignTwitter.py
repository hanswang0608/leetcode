class Twitter:

    def __init__(self):
        self.following = defaultdict(set)   # user: {followees}
        self.tweets = defaultdict(list)     # user: stack of tweets, tweet = (timeStamp, tweetId)
        self.time = 0                       # monotonically increasing timestamp for tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        # push (timestamp, tweetId) onto tweets[userId] stack then increment time
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # make sure user is following themselves
        self.following[userId].add(userId)
        # create minHeap
        # iterate over following[userId] and add each followee's most recent tweet to heap
        minHeap = []
        # O(F) to build heap, F = # of followees
        for followee in self.following[userId]:
            mostRecent = len(self.tweets[followee]) - 1
            if 0 <= mostRecent < len(self.tweets[followee]):
                timestamp, tweetId = self.tweets[followee][mostRecent]
                minHeap.append((timestamp, tweetId, followee, mostRecent - 1))
        heapq.heapify(minHeap)
        ans = []
        # select the most recent tweet 10 times
        # O(10logF)
        while minHeap and len(ans) < 10:
            timestamp, tweetId, followee, nextTweet = heapq.heappop(minHeap)
            ans.append(tweetId)
            if 0 <= nextTweet < len(self.tweets[followee]):
                timestamp, tweetId = self.tweets[followee][nextTweet]
                heapq.heappush(minHeap, (timestamp, tweetId, followee, nextTweet - 1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followeeId to following[followerId]
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from following[followerId]
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)