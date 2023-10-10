# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        
        
        length = 0
        curr = head
        while (curr):
            length += 1
            if curr.next == None:
                curr.next = head
                break
            else:
                curr = curr.next


        break_off = length - abs(k % length)
        
        counter = 0
        iter_node = curr
    
        save_head = None
        
        while (True):
            if counter == break_off:
                save_head = iter_node.next
                iter_node.next = None
                break
            counter += 1
            iter_node = iter_node.next
        return save_head
            