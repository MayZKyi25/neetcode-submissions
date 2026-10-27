# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        #create dummy
        # assign end to dummy
        dummy = ListNode()
        end = dummy

        while list1 and list2: 
            if list1.val < list2.val: 
                # connect end to l1
                # update l1
                end.next = list1
                list1 = list1.next

            else: 
                # connect end to l2
                # update l2
                end.next = list2
                list2 = list2.next
            #update end
            end = end.next 

        end.next = list1 or list2  #stitch it to the rest
        return dummy.next


        # # [1   ->    2     -> 4]
        # # [1   ->    3     -> 5]

        # head1 = list1
        # head2 = list2

        # node2 = head1.next
        

        # print(node2.val)
        




    


        