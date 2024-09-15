"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        cur = dummy
        nodes = {}

        while head:
            newNode = None
            if head in nodes:
                newNode = nodes[head]
            else:
                newNode = Node(head.val)
                nodes[head] = newNode
            randomNode = None
            if head.random and head.random in nodes:
                randomNode = nodes[head.random]
            elif head.random:
                randomNode = Node(head.random.val)
                nodes[head.random] = randomNode
            newNode.random = randomNode
            cur.next = newNode
            cur = cur.next
            head = head.next

        return dummy.next

# hash the actual node objects themselves since values are not unique