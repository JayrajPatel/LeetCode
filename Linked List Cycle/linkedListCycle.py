# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowP,fastP = head, head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP:
                return True
            
        return False