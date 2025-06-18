def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# Intuition:
    # Remember that the original list was SORTED. After the rotation, there is a left and right portion.
    # Imagine parallel lines in the 1st quadrant of the XY-plane that start from different points on the x and y-axis.
    # Use a modified binary search and compare the midpoint to the endpoints to decide whether to
    # search the left portion or the right portion.
    # 2 Cases:
    # Assume we know we are in the left portion of the list. We must decide whether to go left or right.
        # If target is greater than the mid, then obviously the target is in the right portion.
        # However, if the target is smaller than the mid, then the target could be to the left of the mid
        # or in the right portion. To decide, compare the target to the left pointer.
        # If the target is smaller the left pointer, then it must be in the right portion since the
        # left pointer is the smallest element in the left portion.
        # Convince yourself - eg. 4 5 6 7 0 1 2    (target = 0)
        #                         L     M     R
    # Assume know we are in the right portion of the list. We must decide whether to go left or right.
        # If the target is smaller than the mid, then obviously the target is in the left portion.
        # However, if the target is greater than the mid, then the target could be to the right of the mid
        # or in the left portion. To decide, compare the target to the right pointer.
        # If the target is greater than the right pointer, then it must be in the left portion since the
        # right pointer is the greatest element in the right portion.
        # Convince yourself - eg. 4 5 6 7 0 1 2    (target = 5)
        #                         L     M     R
    #
    # Initialize our left and right pointers for the binary search.
    # In the loop, calculate the midpoint. If the mid equals the target, return the index of mid.
    # Otherwise, check if the left pointer is less than or equal to the mid. If it is, then
    # we are in the left portion of the list. Check if the target is greater than the mid
    # or if the target is less than the left pointer. If one of the above is true,
    # then set the left pointer to be mid + 1 to throw the left portion away.
    # If neither are true, then set the right pointer to be mid -1 to throw the right portion away.
    # If the left pointer is not less than or equal to the mid, then check for one of the 2
    # conditions outlined above. If the target is smaller than the mid or if the target is greater
    # than the right pointer, set the right pointer to be mid - 1 to throw the right portion away.
    # If neither are true, then set the left pointer to be mid + 1 to throw the left portion away.
    # When the loop breaks, return -1 to show the target was not found.
