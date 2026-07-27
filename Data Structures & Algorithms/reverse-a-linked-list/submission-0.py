# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        proc = head
        previous = None
        while proc is not None:
            next_node = proc.next
            proc.next = previous
            previous = proc
            proc = next_node
        return previous 
