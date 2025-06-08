from collections import defaultdict
def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            char_arr = [0] * 26
            for char in s:
                char_arr[ord(char) - ord('a')] += 1
            result[tuple(char_arr)].append(s)
        return result.values()

# Intuition:
    # Use a hashmap where we will use tuples of the character count array as keys and a list of the the words as values.
    # Iterate through all the words and create a character count array for each. Since each word will have at most
    # at most 26 unique characters, use an array of length 26.
    # Subtract the ASCII value of the letter 'a' from the ASCII value of the current character, and use that as an index.
    # Convert this resulting count array to a tuple and use this as a key in the hashmap, then append the word to value list.
    # Return the values of the hashmap.

# n = length of longest word, m = number of words
# Time complexity - O(m * n)
# Space complexity - O(m)