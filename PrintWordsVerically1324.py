'''
    Given a string s, return all words vertically in the same order in which they appear in s.
    Words are returned as a list of strings, complete with spaces when necessary.

'''


class Solution:
    def printVertically(self, s):
        words = s.split(" ")

        length_of_longest_word = len(max(words, key=len))

        result = [[' '] * len(words) for i in range(length_of_longest_word)]

        # transpose words
        for i in range(length_of_longest_word):
            for j in range(len(words)):
                if (i < len(words[j])):
                    result[i][j] = words[j][i]

        # remove trailing spaces
        i = length_of_longest_word - 1
        while ((i > -1)):
            j = len(result[i]) - 1
            while ((j > -1) and (result[i][j] == " ")):
                # remove spaces until we reach the first letter
                result[i].pop()
                j -= 1
            i -= 1

        return ["".join(row) for row in result]