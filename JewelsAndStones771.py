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

    #second take at same problem
    def count(self, string):
        counter = {}
        for char in string:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        return counter

    def numJewelsInStones2(self, J: str, S: str) -> int:
        jewels = {char: True for char in J}

        stone_count = self.count(S)
        jewel_count = 0
        for stone in stone_count:
            if stone in jewels:
                jewel_count += stone_count[stone]

        return jewel_count