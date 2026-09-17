class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        def find_kth_node(temp, k):
            for _ in range(k - 1):
                if temp is None:
                    return None
                temp = temp.next

            return temp

        def reverse_k_nodes(temp, next_group):
            prev = None
            curr = temp

            while curr != next_group:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        temp = head
        prev_group_tail = None
        new_head = None

        while temp:

            last_node = find_kth_node(temp, k)

            if last_node is None:
                break

            # Save this BEFORE reversing
            next_group = last_node.next

            # Reverse current group
            group_head = reverse_k_nodes(temp, next_group)

            # Connect previous group to current group
            if new_head is None:
                new_head = group_head
            else:
                prev_group_tail.next = group_head

            # temp is now the tail of reversed group
            temp.next = next_group

            # Save tail for next group
            prev_group_tail = temp

            # Move to next group
            temp = next_group

        return new_head