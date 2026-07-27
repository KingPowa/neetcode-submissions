# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def remove(node, n):
            if node is None:
                # We are at the end: start decrementing n
                return n, node

            current_node, _ = remove(node.next, n)
            if current_node == 0 and node.next is not None:
                # We called remove on the node to remove!
                node.next = node.next.next
            elif node.next is None:
                node = None
            return current_node - 1, node

        n, head = remove(head, n)
        if n == 0:
            return head.next if head is not None else None
        return head  