"""
    Leetcode Problem: 49,
    Written By: Taré Gaskin,
    Written On: 11/23/2018

"""

"""
    Algorithm2
    Status: Sufficient
    Time to Status: ~ 1hr,

    Algorithm1
    Status: Insufficient:  It passes 100 / 101 test cases. The last one is a complexity stress test which I fail.
    Time To Status: 1hr 40mins, 1.50hrs


""""





# Given Test Case
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


# class Solution:


# Objective:  Given an array of strings, group anagrams together.
# Anagrams are words with the same number of letters, and the same count of each letters.
# Thus, to check if two words are anagrams check that for each letter they have the same countself.






# Algorithm 2
"""
    Complexity: Time: O( N * k*log(k) ), Space( N ) , N is number of strings in input array, k is length of longest string.

    Iterate through the strings,
        Use the fact that for n > 2 words are anagrams if they are the same character sequence when sorted and
            Use a hashmap to check for equality,
        Append Acorrdingly,

    Return the grouping.

    --

    Takeaway:
         - Optimization doesn't matter until you have a solution.
         - Be mentally prepared to write a brute force step by step solution. The optimized solution often enough
         exists within the brute force solution.
         - Be prepared to work on a problem for an hour, until I start to really get the hang of things, 


    I think the key thing here was realizing that I could decrease the complexity of my eqaulity check by
    using a hashmap. This idea lead me to the idea of coming up with an anagramID that would quickly let me check
    eqaulity in anagram terms. Then I looked at the solution and saw that the sorted string was a handy id.

"""

    def groupAnagrams(self, strings ):
        anagramGroups = {}

        for string in strings:
            stringAnagramID = ''.join( sorted( string ) )
            if stringAnagramID not in anagramGroups:
                anagramGroups[ stringAnagramID ] = [ string ]
            else:
                anagramGroups[ stringAnagramID ].append( string )

        # print( anagramGroups )
        return [ group for group in anagramGroups.values() ]















    # Algorithm1:
    """
        Complexity: O(n * n * k), where n is the length of the array given, and k is the longest string in the array.

        Allocate a 2d dynamic arary that we will populate and output,
        Iterate through the given strings:

        enumerate and count each letter of the string, *

        check if this count is unique: compare to all counts we have already,
            if we find a match:
                add the string to the array that corresponds to the count we found,
            else we don't find a match:
                save the count, *
                add teh string to a new array that corresponds to this unique count

        return the 2d output array
    """



class anagramGroup:
    def countLetters(self, string ):
        # :type string: str
        # :rtype:

        letterCounts = {}

        for letter in string:
            if letter in letterCounts:
                letterCounts[ letter ] += 1
            else:
                letterCounts[ letter ] = 1
        return letterCounts

    def __init__(self, word):
        self.totalCount = len( word )
        self.letterCounts = self.countLetters( word )
        self.words = [ word, ]

    def isAnagram( self, otherAnagramGroup  ):
        if self.totalCount != otherAnagramGroup.totalCount:
            return False # create a new word group
        for letter, count in self.letterCounts.items():
            if letter in otherAnagramGroup.letterCounts.keys():
                if otherAnagramGroup.letterCounts[ letter ] != count:
                    return False
            else: # if the one word contains a letter that isn't in the other immediately know it's false
                return False
        return True

    def addWord(self, word):
        self.words.append( word )
        return

def groupAnagrams(self,  strings ):
    anagramGroups = []

    for string in strings:
        ag = self.anagramGroup( string )

        match = False
        for group in anagramGroups:
            if group.isAnagram( ag ):
                group.addWord( ag.words[0] ) # generalization flaw
                match = True
                break
        if (not match):
            anagramGroups.append( ag )


    return [ retAG.words for retAG in anagramGroups  ]



print( groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]  ) )
