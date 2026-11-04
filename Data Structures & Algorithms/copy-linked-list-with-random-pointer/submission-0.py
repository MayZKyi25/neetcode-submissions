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
        # 2-pass Solution

        cur = head
        mappings = { None: None } # key will be orig Node, value will be copied Node. we add this None mapping to handle edge cases where we ask for mappings[None]

        # copy each node from input list, but don't handle next/random ptrs yet
        while cur:
            copy = Node(cur.val)
            mappings[cur] = copy

            cur = cur.next    

        cur = head
        # for each orig node, find its copy & update the copy's next/random ptrs using the map to get the copies of the orig node's next/random ptrs
        while cur:
            copy = mappings[cur]
            copy.next = mappings[cur.next]
            copy.random = mappings[cur.random]

            cur = cur.next

        return mappings[head]

        
    


        