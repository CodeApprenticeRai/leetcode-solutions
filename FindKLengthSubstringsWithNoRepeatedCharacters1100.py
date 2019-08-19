'''
    Approach:
        Set up a k-wide rolling window along S,
        set up a counter for all the found k_length substrings with no repeated characters
            For in substring in the rolling window: O(n)
                determine if substring has repeating characters, O(substring) || O(1)
                    if doesn't:
                        increment counter
                k_i, k_j += 1
'''
from collections import deque


class Solution:
    def numKLenSubstrNoRepeats2(self, S, K):
        match_counter = 0
        i = 0
        j = K - 1
        letter_count_cache = {}

        rolling_substring = deque()
        while ((j < len(S))):
            # popleft to preserve uniqueness
            while ((j > i) and (S[j] in letter_count_cache)):
                del letter_count_cache[rolling_substring.popleft()]
                i += 1

            # append
            rolling_substring.append(S[j])
            letter_count_cache[S[j]] = True

            if (len(rolling_substring) == K):
                match_counter += 1
                del letter_count_cache[rolling_substring.popleft()]
                i += 1

            j += 1
        return "INCOMLPETE" #match_counter

        def numKLenSubstrNoRepeats(self, S, K):

            match_counter = 0
            k_i = 0
            k_j = K
            # substring = deque()

            while (k_j <= len(S)):
                substring = S[k_i:k_j]
                letter_count_cache = {}
                has_repeating_characters = False

                # O(substring), can be O(1)
                for letter in substring:
                    if letter in letter_count_cache:
                        has_repeating_characters = True
                        break
                    else:
                        letter_count_cache[letter] = 1

                if not has_repeating_characters:
                    match_counter += 1
                k_i += 1
                k_j += 1

            return match_counter