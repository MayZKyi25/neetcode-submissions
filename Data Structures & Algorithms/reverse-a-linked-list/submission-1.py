# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head 
        prev = None
        while cur: 
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp 
        return prev


        '''
        None         1   -->    2      -->      3     -->      4
        prev        cur      cur.next
                    prev        temp
                                cur

        None  <----   1          2      -->      3     -->      4
        prev         cur      cur.next
                                temp 

        None <---     1    <---- 2  <---- 3 <-----4
        '''


            


        # head 
        # prev

        # if head is empty:
            # return []

        #   1   2 ---> 3 --->  4
        # head.      temp
        # cur  

        # <---- 1 <--- 2      3   <---- 4
        # prev        cur     temp
        
        # <---- 1 <--- 2      3   <---- 4
        #           cur     temp
        #           prev 

        #     <---- 1 <--- 2      3   <---- 4


    
  




     

    



        
          
            

        