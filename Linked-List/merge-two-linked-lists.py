# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
        node = ListNode(0)
        dummy = node
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next


# Intuition:
    # Use a dummy node and an iterator pointer to compare and traverse the 2 lists.
    # Create a new dummy node and assign it 2 pointers, a dummy (to keep track of beginning) and an iterator pointer.
    # Next, our main loop needs to run while we can compare the nodes of the 2 lists.
    # There are 2 cases which we need to consider:
    # If the list1 node is less than the list2 node, we need to add the list1 node to the output list.
    # To do so, set the the iterator's next pointer to the list1 node and advance the list1 pointer.
    # If the list1 node is greater than the list2 node, we must do the same steps as above but with the list2 node.
    # Regardless of case, we must advance the iterator pointer.
    # When the loop breaks, we must add whatever is left of list1 or list2, if anything.
    # Return the next pointer of the dummy pointer to return the output list.

# n = # of nodes in list1, m = # of nodes in list2
# Time complexity - O(n + m)
# Space complexity - O(1)