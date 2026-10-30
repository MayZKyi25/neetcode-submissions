# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # init dummy node
        # init left, right both at dummy

        # move right N steps
        # move left and right together 1 node at a time (so we always maintain distance of N nodes between them), and we stop when right reaches last node. now left should be stopped at the node right before the node we want to remove

        # remove the node after left (left.next = left.next.next)
        # return dummy.next (can't just return head bc edge case where we remove head)

        dummy = ListNode(0, head)
        left = right = dummy

        for i in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        