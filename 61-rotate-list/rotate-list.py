class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        temp = head
        length = 1

        while temp.next:              # change 1
            temp = temp.next
            length += 1

        temp.next = head

        k = k % length
        iteration_count = length - k

        iterate = head              # change 2

        for i in range(iteration_count - 1):  # change 3
            iterate = iterate.next           # change 4

        head = iterate.next
        iterate.next = None

        return head