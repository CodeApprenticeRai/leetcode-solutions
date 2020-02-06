'''
Given a string s, fidn the length of the longest substring t that contains at most 2 distinct characters
'''
from collections import deque # to optimize the cost of popping from the front of the substring

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
	
	if not s:
		return len(s)
	else:
		#create a substring, create a map to keep the distinctCharacterCount, create a variable to hold the lengthOfLongestSubstring
		_t = deque()
		distinctCharacterCount = {}
		lengthOfLongestSubstring = 0

		for i in range(len(s)):
			#consider the number of distinct characters in the array, and the characters themselves
			#if the number of distinct characters in _t == 0: just add s[i] to _t and increment the distinct character count
			if (len(distinctCharacterCount) == 0):
				_t.append(s[i])
				distinctCharacterCount[s[i]] = 1
		
			#if the number of distinct characters in _t == 1: add s[i] to _t and increment te distinct character count
			elif (len(distinctCharacterCount) == 1):
				_t.append(s[i])
				if s[i] in distinctCharacterCount:
					distinctCharacterCount[s[i]] += 1
				else:
					distinctCharacterCount[s[i]] = 1

			#if the number of distinct characters in _t == 2: remove characters from _t and decrement the distinct character count until the distinct character count is < 2: then add s[i] to _t and increment the distinct character count
			elif ( (len(distinctCharacterCount) == 2) ):
				if (s[i] in distinctCharacterCount ):
					_t.append(s[i])
					distinctCharacterCount[s[i]] += 1
				else:
					while ( len(distinctCharacterCount) == 2 ):
						beingDeleted = _t.popleft()
						distinctCharacterCount[beingDeleted] -= 1
						if distinctCharacterCount[beingDeleted] == 0:
							delete distinctCharacterCount[beingDeleted]
			l
			#update the length of the longest substring
			lengthOfLongestSubstring =  max( lengthOfLongestSubstring, len(_t) )
	
		return lengthOfLongestSubstring