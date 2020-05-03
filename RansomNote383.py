'''
    This is a subset test:
    Is ransomNote a subset of magazine


'''


class Solution:
    def count(self, string):
        counter = {}
        for char in string:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        return counter

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCount = self.count(ransomNote)
        magazineCount = self.count(magazine)

        for letter in noteCount:

            if ((letter not in magazineCount) or (magazineCount[letter] < noteCount[letter])):
                return False
        return True