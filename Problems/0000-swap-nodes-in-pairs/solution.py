# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummyNode = ListNode(-1)
        dummyNode.next = head
        prev = dummyNode
        while prev and prev.next.next:
            first = prev.next
            second = first.next
