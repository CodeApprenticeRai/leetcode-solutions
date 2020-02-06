class Solution:
    def longestStrChain(self, words):
        solution_cache = {}
        words.sort(key=len)
        print(words)
        _global_max = None

        for word in words:
            solution_cache[word] = max([ solution_cache.get( word[:i] + word[i + 1:], 0) + 1 for i in range(len(word))  ])

            if ((type(_global_max) == type(None)) or (_global_max < solution_cache[word])):
                _global_max = solution_cache[word]

        return _global_max

sol = Solution()
print(sol.longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))