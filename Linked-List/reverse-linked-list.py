def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Intuition:
    # Set the current node's next pointer to the previous node. This will reverse the linked list.
    # We need two pointers, a prev and a curr, which we will initialize to point to null and to the head.
    # Traverse the linked list using curr and prev.
    # Save a pointer to the node after the current node (called temp).
    # Set the current node's next pointer to the prev pointer. (This is where the reversal happens.)
    # Set prev equal to curr to advance prev.
    # Set curr equal to temp to advance curr.
    # After the loop breaks, prev will be pointing to the new head of the reversed list. Return it.

# Time complexity - O(n)
# Space complexity - O(1)
