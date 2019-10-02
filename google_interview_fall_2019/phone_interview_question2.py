'''
You
have
two
strings: A and B
Can
you
concatenate
subsequences
of
string
A
to
form
string
B?
What is the
minimum
number
of
subsequences
required?

A: xyz
xyz + yz + x
B: xyzyzx
yes

A: wy
B: wxyx
no

A -> B

‘’’

‘’’
Start
at
the
beginning
of
the
string,
challenge_substring = “”,
substring_memo = {A[:i + 1]: True for i in range(len(A))},

for i in range(len(A)):
    substring_memo[A[i:]] = True

i = 0
_minimum_substring_count = 1

while (i < len(B)):
    if (challenge_substring == “” or challenge_substring is in our substring_memo)
        add
        character
        B[i]
        to
        challenge_substring
i += 1
else our
challenge_substring is not in our
memo:
if B[i] not in our substring_memo:
    return -1
challenge_substring = “”
minimum_substring_count += 1
return minimum_substring_count
'''

class Solution:
    def naive_solution(self, A, B):
        A_memo = {_char: True for _char in A}
        for i in range(len(B)):
            if B[i] not in A_memo:
                return False
            return True


    def all_substrings(self, string):
        memo = {}

        for i in range(len(string)):
            for j in range(i, len(string) + 1):
                memo[string[i:j]] = True
        return memo


    def minimum_number_of_subsequences_for_concatenation(self, A, B):
        if not self.naive_solution(A, B):
            return -1

        i = 0
        challenge_substring = ""
        substring_memo = self.all_substrings(A)

        minimum_substring_count = 1

        while (i < len(B)):
            if ((challenge_substring == "") or (challenge_substring + B[i] in substring_memo)):
                challenge_substring += B[i]
                i += 1
            else:
                if (B[i] not in substring_memo):
                    return -1
                challenge_substring = ""
                minimum_substring_count += 1
        return minimum_substring_count

sol = Solution()

print( sol.minimum_number_of_subsequences_for_concatenation("xyz", "xyzyzx") == 3  )
print( sol.minimum_number_of_subsequences_for_concatenation("wy", "wxyx") == -1 )