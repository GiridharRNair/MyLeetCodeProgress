# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        outList = ListNode()
        head = ListNode()
        
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        
        if list1.val > list2.val:
            head = ListNode(list2.val)
            list2 = list2.next
        else:
            head = ListNode(list1.val)
            list1 = list1.next
            
        outList = head
            
        while list1 and list2:
            if list1.val > list2.val:
                outList.next = ListNode(list2.val)
                outList = outList.next
                list2 = list2.next
            else:
                outList.next = ListNode(list1.val)
                outList = outList.next
                list1 = list1.next
        
        if list1:
            outList.next = list1
        else:
            outList.next = list2
                
        return head
        
                