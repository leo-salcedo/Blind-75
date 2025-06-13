from collections import defaultdict
def characterReplacement(self, s, k):
        char_freq = defaultdict(int)
        max_freq = 0
        max_length = 0
        l = 0
        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_freq = max(max_freq, char_freq[s[r]])
            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length


# Intuition:
    # A couple of brief ideas: The window length is calculated by r - l + 1.
    # Since we want to maximize the window length, we want to find the max frequency of any one character.
    # This will minimize the number of replacements.
    # To calculate the number of replacements we must make in any given window, subtract the max frequency seen so far
    # from the window length. If the window is valid, the result of this subtraction will be less than or equal to k.
    # A new max window length will be found if and only if a new max frequency is found. This means we do not need 
    # to alter the max frequency other than increasing it (ie. only getting larger).
    # 
    # Use a hashmap (to track the max frequency) and a sliding window approach to calculate the max window length.
    # Set the left pointer at the start of the string. Loop through all characters in the string.
    # For each character, increment their count in the hashmap. Update the max frequency accordingly.
    # Then, while the window length - the max frequency is greater than k (ie. while the window is invalid because 
    # more than k replacements are needed), decrement the count of the character at the left pointer since it is no longer 
    # considered in the new window and shrink the window by advancing the left pointer.
    # Once the above loop breaks, then update the max window length accordingly.