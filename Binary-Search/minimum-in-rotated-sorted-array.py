def findMin(self, nums):
        result = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result


# Intuition:
    # Notice that the original list is SORTED. After the rotation, we have 2 portions of the list,
    # and the minimum must be in one of the 2 portions.
    # After the rotation, everything before the pivot is greater than or equal to the first element (of the rotated list),
    # and everything afte the pivot is less than or equal to the last element.
    # Track the current minimum found and decide whether to search the left or right portion of the list.
    # Use a modified binary search to decide which portion of the list to throw away.
    #
    # Initialize our left and right pointers and set the result to the first element in the list.
    # Initialize our while loop where our logic will reside.
    # Compare the left and right pointers. If the left is less than the right, then we are in a sorted portion.
    # Therefore, the minimum will be the left pointer, so update result and break.
    # Otherwise, calculate the midpoint, and update result accordingly.
    # If the mid pointer is greater than the left pointer, then the left portion is strictly ascending.
    # Therefore, the pivot (and the min) must be in the right portion. Set the left equal to mid + 1
    # to discard the left portion and search the right portion.
    # Otherwise, the right portion is strictly ascending. Therefore, the pivot (and the min) must be
    # in the left portion. Set the right equal to mid - 1 to discard the right portion and search
    # the left portion.

# Time complexity - O(log(n))
# Space complexity - O(1)
