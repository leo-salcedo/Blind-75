def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# Intuition:
    # Use a two pointer approach to advance through the string and compare characters to ensure validity.
    # Initialize a left and right pointer at opposite ends of the string.
    # While the left is less than the right, check if each character at each pointer is valid (ie. alphanumeric).
    # If not, move pointer closer to middle (increment left or decrement right) and restart loop using continue.
    # If both characters are valid, then convert characters to lower case and compare them.
    # If they are not the same, then we cannot have a palindrome, so return false.
    # Otherwise move pointers closer to middle (increment left and decrement right).
    # If the loop above (l < r) breaks, then string is a palindrome. Return true.

# Time complexity: O(n)
# Space complexity O(1)