def threeSum(self, nums):
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return result


# Intuition:
    # Defn: Anchor - an index in the list that does not move and is always used the the three sum calculations.
    # Defn: Resultant list - the remainder of the original list that is to the right of the anchor, as space permits.
    # E.g.: [1, 2, 3, 4]. Say 1 is the anchor. Therefore, [2, 3, 4] is the resultant list. We will check all possible
    # unique triplets of 1 + x + y = 0.
    #
    # Use a two pointer approach combined with this anchor idea to calculate unique triplets that add to 0.
    # First sort the array. This is necessary to help us avoid duplicate triples in our result list.
    # Begin looping (i) through the list. There are a few things we need to check for before initializing our two pointers.
    # First, check if the current number is greater than 0. If it is, then no more triples that add to 0 are possible since
    # all subsequent numbers are also positive (because of sorting). Break from the loop
    # Secondly, check if the current number is equal to the previous number. If it is, then increment i and restart the loop
    # using continue. This prevents duplicate triplets.
    # If none of the above applies, then initialize the left and right pointers to the beginning and end of the resultant list,
    # respectively. I.e. l = i + 1, r = len(nums) - 1.
    # Calculate the sum of the the triplet and compare to 0. If the sum is 0, then add the triplet to the result list.
    # Move the left and right closer to the center of resultant list by incrementing and decrementing, respectively.
    # Then, make another loop with two conditions: while nums[l - 1] == nums[l] (same duplicate prevention logic as above)
    # and while l < r, so the left does not overtake the right prematurely.
    # If the sum is not equal to 0, we have two cases: The sum is too large or too small.
    # If the sum > 0, decrement right (to shrink sum). If sum < 0, increment left (to grow sum).

# Time complexity: O(n^2)
# Space complexity: Idk
