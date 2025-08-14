def removeNthFromEnd(self, head, n):
    # size = 0
    # curr = head
    # while curr:
    #     size += 1
    #     curr = curr.next
    
    # if size - n == 0:
    #     return head.next

    # prev, curr = None, head
    # for i in range(size - n):
    #     temp = curr.next
    #     prev = curr
    #     curr = temp

    # prev.next = curr.next
    # return head

    dummy = ListNode(0, head)
    left, right = dummy, head
    for i in range(n):
        right = right.next

    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    return dummy.next


# Two-pass solution also above.

# Intuition:
    # Use a dummy node to create a starting gap of 1 (ie. number of links) between the
    # left and right pointers. Start the left at the dummy and the right at the head.
    # Advance the right pointer n nodes to create a gap of n + 1.
    # Then, until the right pointer reaches the end of the list, advance both pointers
    # in tandem, maintaining this gap of n + 1.
    # When the loop breaks, the left pointer will be right before the nth node from the end.
    # Remove the nth node from the end and return the node after the dummy.

# Time complexity - O(n)
# Space complexity - O(1)



