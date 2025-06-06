def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []

# Intuition:
    # Use a hashmap to keep track of complements and indices.
    # Loop through array and calculate complement at each index.
    # If the complement is in the hashmap, then there must be another number that when added to the current number = target.
    # Otherwise add current number to hashmap with value as index.

# Time complexity - O(n)
# Space complexity - O(n)