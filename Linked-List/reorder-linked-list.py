def reorderList(self, head):

    def reverseList(node):
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    head2 = reverseList(slow.next)
    slow.next = None

    while head2:
        tmp1, tmp2 = head.next, head2.next
        head.next = head2
        head2.next = tmp1
        head, head2 = tmp1, tmp2


# Intuition:
    # Notice that after we reorder the list, the nodes are in order of 0, n - 1, 1, n - 2, ...
    # Check with list 0, 1, 2, 3, 4, 5, 6 --> 0, 6, 1, 5, 2, 4, 3. Convince yourself.
    # Once we see this, we can logically conclude that to reorder the list, we must split the list
    # in half, reverse the second half, and then merge the first half and the reversed second half.
    # First things first, write a basic function that reverses a linked list and returns the new head.
    # Explantion is omitted for the sake of brevity.
    # Secondly, we can use a fast and slow pointer to reach the middle of the list. Once the fast pointer
    # reaches the end of the list, the slow pointer will be at the node before the "head" of the sublist
    # we need to reverse.
    # Call our reverse function with the node after the slow pointer and split the list into the 2 halves.
    # Then, merge the 2 halves using the second "head" as a condition for our while loop.
    # Imagine the 2 halves one on top of the other. When merging, we are making a new list
    # whose pointers look like a zig zag, similar to shoe laces.


# Time complexity - O(n)
# Space complexity - O(1)