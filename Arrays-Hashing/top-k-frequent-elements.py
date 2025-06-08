from collections import defaultdict
def topKFrequent(self, nums, k):
        n = len(nums)
        count = [[] for i in range(n + 1)]
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for num, freq in hashmap.items():
            count[freq].append(num)
        result = []
        for j in range(len(count) - 1, 0, -1):
            for num in count[j]:
                result.append(num)
                if len(result) == k:
                    return result
                

# Intuition:
    # Use a bucket sorting approach.
    # Initialize a list of lists (called count) of size n + 1, where we will use a number's frequency as an index in count,
    # and add that number into the list at that index.
    # To do that, first create a frequency map for the given list.
    # Create a result list, and loop backwards in the count list.
    # At each index in count, add all the elements in that list to result until the length of result equals k.

# Time complexity - O(n)
# Space complexity - O(n)