def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        max_amt = 0
        while l < r:
            curr_amt = min(heights[l], heights[r]) * (r - l)
            max_amt = max(max_amt, curr_amt)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_amt


# Intuition:
    # Use a two pointer approach to move the pointer that is currently limiting (ie. the lowest height) to find the max possible amount.
    # Initialize two pointers, a left and a right, to opposite ends of the list.
    # While left is less than right, calculate the current amount by taking minimum of the heights at the pointers and multiplying by 
    # difference of right and left. We are essentially calculating the area of a rectangle.
    # Update the max amount found accordingly.
    # If the height at the left is less than the height at the right, this means that the left height is limiting the amount.
    # Bring the left pointer close to the center by incrementing it to find a new amount.
    # Otherwise, bring the right pointer to the center by decrementing it to find a new amount.
    # Return the max amount found.

# Time complexity: O(n)
# Space complexity: O(1)
