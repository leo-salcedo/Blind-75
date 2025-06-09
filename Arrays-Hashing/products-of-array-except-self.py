def productExceptSelf(self, nums) :
        n = len(nums)
        prefix_prod = [0] * n
        suffix_prod = [0] * n
        prefix_prod[0], suffix_prod[n - 1] = 1, 1
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            suffix_prod[j] = suffix_prod[j + 1] * nums[j + 1]
        output = [0] * n
        for k in range(n):
            output[k] = prefix_prod[k] * suffix_prod[k]
        return output


# Intuition:
    # Use a prefix and suffix product arrays to keep track of the product of all numbers before and after index i, exclusive.
    # Initialize the two prefix and suffix arrays to be the same size at the original list, and set the first and last indices
    # to be 1, respectivelly.
    # For the prefix array, loop forwards in the original list starting from the second element, and set the current index in 
    # the prefix array to be the product of the previous element ([i - 1]) in the prefix array and the previous element in the original list.
    # For the suffix array, loop backwards in the in the original list starting from the second to last element, and set the current
    # index in the suffix array to be the product of the next element ([i + 1]) in the suffix array and the next element in the original list.
    # Finally, create another list and set its indices to be the product of the same index in the prefix and suffix arrays.

# Time complexity - O(n)
# Space complexity - O(n)