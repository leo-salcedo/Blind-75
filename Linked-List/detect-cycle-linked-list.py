def hasCycle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


# Intuition:
    # Use a 'tortoise and hare' two pointer approach to determine if there's a cycle.
    # Initialize a slow and fast pointer. If at any point the pointers are at the same node, then
    # the list has a cycle.
    # While the fast pointer can advance, check if the pointers are at the same node.
    # If they are, then return true. Otherwise, advance the slow pointer one node
    # and the fast pointer 2 nodes.
    # When the loop breaks, return false, as there is no cycle in the list.

# Time complexity - O(n)
# Space complexity - O(1)
