'''
    given (int i, string S, string x, string y) if x starts at i in S replace x in S with y, else do nothing
'''

'''
    Strategy:

        zip indexes, to turn i, x, y into a single map of objects rather than 3 lists. sort by index increasing.
        create a new string that will be returned as the transformed_S.
        iterate through i in range(len(S)):
            if i not in indexes:
                transformed_S += S[i]
            elif i in indexes:
                if ( (i+len(x) <= len(S)) and (S[i:i+len(x)] == x[i] ) ):
                    transformed_S += y[i]
                    i += len(x)
            return 
'''


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        get = {}
        for _i in range(len(indexes)):
            get[indexes[_i]] = {
                "x": sources[_i],
                "y": targets[_i]
            }

        i = 0
        transformed_S = ""
        while (i < len(S)):
            if ((i in indexes) and ((i + len(get[i]["x"]) <= len(S)) and (S[i:i + len(get[i]["x"])] == get[i]["x"]))):
                transformed_S += get[i]["y"]
                i += len(get[i]["x"])
            else:
                transformed_S += S[i]
                i += 1

        return transformed_S

def test():
    sol = Solution()
    sol.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"])
    # sol.findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"])
    # sol.findReplaceString()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=100))