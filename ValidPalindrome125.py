'''
    Given a string determine if it's a palindrome,
    considering only alphanumberic characters and ignoring cases
'''

'''
    create a new string that just exists of alphanumeric characters.

    consider the length of this new string
    if the length is even, we start are pointers at (len(s) / 2) - 1, (len(s) / 2)
    If the length is odd, we start our pointers at floor(len(s) / 2), (len(s) / 2),


    while the rightmost pointer < len(new_string): iterate: 
        if cleaned_string[li] != cleaned_string[ri]:
            return False
        l1 -= 1
        ri += 1


'''

import math


class Solution:
    def isPalindrome(self, s):
        cleaned_string = ""

        for char in s:
            if char.isalnum():
                cleaned_string += char

        li = None
        ri = None
        if ((len(cleaned_string) % 2) == 0):
            li = int((len(cleaned_string) / 2) - 1)
            ri = int(len(cleaned_string) / 2)
        else:
            li = int(math.floor(len(cleaned_string) / 2)) -1
            ri = int(math.ceil(len(cleaned_string) / 2))

        while (ri < len(cleaned_string)):
            l = cleaned_string[li].lower()
            r = cleaned_string[ri].lower()
            if cleaned_string[li].lower() != cleaned_string[ri].lower():
                return False
            li -= 1
            ri += 1
        return True

sol = Solution()
print( sol.isPalindrome("A man, a plan, a canal: Panama") )