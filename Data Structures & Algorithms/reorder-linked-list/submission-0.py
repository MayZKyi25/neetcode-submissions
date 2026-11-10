# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # None<----4 --> 5 --> 6 
        # prev    cur 
        #         temp

        # find the middle
        slow = head
        fast = head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        # init cur as the 1st node at the 2nd half 
        cur = slow.next
        slow.next = None
        prev = None
        while cur: 
            temp = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp

        # stictch one node from 1st half and one from 2nd half
        # 2 ----> 4  |  8 ---> 6 ---> None (after reversing) |  None<--6<---8 
        # first        prev
        # 2 ----> 8 --> 4 ----> 6 ---> None
        # first   prev

        first = head
        second = prev
        while second: 
            ptr1 = first.next
            ptr2 = second.next
            first.next = second
            second.next = ptr1 
            first = ptr1
            second = ptr2
          
            

        



        
        