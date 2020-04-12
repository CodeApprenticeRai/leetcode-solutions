class Solution:

    def isHappy(self, n: int) -> bool:
        return self._isHappy(n, {})

    def _isHappy(self, n, visited_cache):
        if n == 1:
            return True

        if n in visited_cache:
            return False

        visited_cache[n] = True
        squared_sum = 0
        for digit in str(n):
            squared_sum += int(digit) ** (2)

        return self._isHappy(squared_sum, visited_cache)