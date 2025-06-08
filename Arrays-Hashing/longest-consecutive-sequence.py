def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            if (num - 1) not in nums_set:
                current = 1
                while (num + current) in nums_set:
                    current += 1
                max_length = max(current, max_length)
        return max_length


# Intuition:
    # We can identify the start of a sequence if for any number, number - 1 does not exist in the list. This is important.
    # Loop through all the numbers, and check if that number - 1 exists in the list (which has been converted for to a
    # set for O(1) lookups)
    # If number - 1 does not exist, then the start of a sequence has been identified.
    # To find the length of the sequence, loop while the original number + an offset exists in the array. (eg. if start is 3, then
    # while 4, 5, 6... exist.)
    # Then, compare to the max length found so far, and update accordingly.
    # When all loops break, then return the max length.
