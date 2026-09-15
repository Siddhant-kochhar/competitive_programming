# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        if not fast.next:
            return None
        else:
            slow, fast = head,head
            fast = fast.next.next

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            slow.next = slow.next.next
            return head
