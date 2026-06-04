# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr=[None]        
        current=head
        while current:
            if current not in arr:
                arr.append(current)
            else:
                return True
            current=current.next
        return False
            

        