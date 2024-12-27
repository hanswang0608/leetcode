class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()

        for card in hand:
            if card not in counter:
                continue
            for i in range(card, card+groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    del counter[i]
        
        return True

# something with sorting
# [1,2,2,3,3,4,4,5]