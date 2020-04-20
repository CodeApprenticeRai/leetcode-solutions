'''
    Given two words: to test if they are anagrams every letter in string1 is in string2
    and every letter in string2 is in string1 then they are anagrams.
    This property is transititive if a is an anagram of b, and c is anagram of b, then  a is an anagram of c.

    The thing is, this could get really bad time wise if not done right.

    if none of the words are anagrams, for every new word, we have to compare it to every other word,

    its n^(2) comparisions AND we have to scan each word to their full length

    To get the time down...

'''

class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = {}

        for string in strs:
            string_is_an_anagram = False
            sorted_string = str(sorted(string))
            for anagram_test_string in anagram_groups:
                string_is_an_anagram = sorted_string == anagram_test_string
                if string_is_an_anagram:
                    anagram_groups[anagram_test_string].append(string)
                    break
            if (not string_is_an_anagram):
                anagram_groups[sorted_string] = [string]

        return [anagram_groups[key] for key in anagram_groups]