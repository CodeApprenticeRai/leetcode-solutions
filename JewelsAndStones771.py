class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        for char in J:
            jewels[char] = True

        jewelCount = 0

        for char in S:
            if char in jewels:
                jewelCount += 1
        return jewelCount