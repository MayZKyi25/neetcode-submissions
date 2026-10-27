# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head 
        # prev

        # if head is empty:
            # return []

        #   0   1 ---> 2 --->  3
        # head.      temp
        # cur  

        # <---- 1 <--- 2      3   <---- 4
        # prev        cur     temp
        
        # <---- 1 <--- 2      3   <---- 4
        #           cur     temp
        #           prev 

        #     <---- 1 <--- 2      3   <---- 4
        #                       temp
        #           prev        cur 
              


        cur = head
        prev = None

        while cur: 
            temp = cur.next # 1 to 2
            cur.next = prev # 2 to 1
            prev = cur #2
            cur = temp # 2
        return prev
        






     

    



        
          
            

        