from collections import defaultdict
def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq_s, freq_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
        return freq_s == freq_t


# Intuition:
    # Obviously, words that are anagrams must be of the same length.
    # Create frequency maps for each of the words and compare said maps.

# Time complexity - O(n)
# Space complexity - O(n)