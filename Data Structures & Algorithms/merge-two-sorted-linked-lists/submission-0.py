# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1, temp2 = list1, list2

        dummy = ListNode(0)

        cur = dummy

        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                cur.next = temp1
                temp1 = temp1.next
            
            else:
                cur.next = temp2
                temp2 = temp2.next

            cur = cur.next

        if temp1 != None:
            cur.next = temp1
        else:
            cur.next = temp2

        return dummy.next



