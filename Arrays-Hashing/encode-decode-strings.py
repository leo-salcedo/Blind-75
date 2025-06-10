def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result


# Intuition:
    # Encode:
        # Loop through all the words.
        # To separate the words, place their length (number) and a special character (eg. '#') and then the word into the result word.
        # This way, we can ensure that we can differentiate between word lengths and regular numbers.

    # Decode:
        # Loop through the given string.
        # Set a current pointer (j) to the given index (i).
        # While j does not point to the special character, advance it. When the loop breaks, the substring [i:j] will represent
        # the length of the current word.
        # Set i to be one more than j. Now, i is at the first character of the word.
        # Set j to be the sum of i + length, calculated earlier. j is at the last character of the word.
        # Append the substring of [i:j] to the result list, and set i = j to restart the process for the next word.


# m = sum of lengths of all words, n = number of strings.
# Time complexity:
    # Encode: O(m)
    # Decode: O(m)

# Space complexity:
    # Encode: O(m + n)
    # Decode: O(m + n)
        