# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        size=0
        while current:
            size+=1
            current=current.next
        length=size-n
        i=0
        current=head
        if size == n:
            return head.next
        if length==1:
            return None
        while i<length-1:
            current=current.next
            i+=1
        ##node=current.next
        ##current.next=node.next
        ##node.next=None
        node = current.next
        current.next = node.next
        node.next = None
        return head

