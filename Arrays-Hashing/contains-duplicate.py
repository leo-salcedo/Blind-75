def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Intuition:
    # Use a hashset (allows for O(1) lookups) to check if number has been seen.
    # Loop through all the numbers and check if the number is in the hashset.
    # If it is, then the number has already been seen, so return true.
    # Otherwise, add it to the hashset.
    # If the above loop breaks, then all numbers appeared exactly once. Return false.
    
# Time complexity - O(n)
# Space complexity - O(n)