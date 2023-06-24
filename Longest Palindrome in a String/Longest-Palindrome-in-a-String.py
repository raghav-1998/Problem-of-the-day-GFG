#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # Preprocess the string to insert special characters
        # to handle even-length palindromes
        modified_string = self.addSpecialCharacters(S)
        n = len(modified_string)
        P = [0] * n  # P[i] stores the length of the palindrome centered at index i
        center = 0  # Center of the current longest palindrome
        right = 0  # Right boundary of the current longest palindrome

        for i in range(n):
            # Mirror index of the current index i
            mirror = 2 * center - i

            # Check if the current index is within the right boundary
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Expand around the current index to find the palindrome length
            while (
                i + P[i] + 1 < n
                and i - P[i] - 1 >= 0
                and modified_string[i + P[i] + 1] == modified_string[i - P[i] - 1]
            ):
                P[i] += 1

            # Update the center and right boundary if necessary
            if i + P[i] > right:
                center = i
                right = i + P[i]

        # Find the maximum length palindrome and its center index
        max_len = max(P)
        center_index = P.index(max_len)

        # Extract the longest palindromic substring from the modified string
        start = (center_index - max_len) // 2
        end = start + max_len

        return S[start:end]

    def addSpecialCharacters(self, S):
        # Helper function to preprocess the string
        # Inserts special characters between characters and at the ends
        modified_string = ['#']
        for ch in S:
            modified_string.append(ch)
            modified_string.append('#')
        return ''.join(modified_string)