class Solution:
    def change(self, amount):
        if (amount == 0):
            return 0
        if amount in self.memo:
            return self.memo[amount]
        else:
            minChange = float('inf')
            _change = float('inf')
            for coin in self.coins:
                if (amount - coin >= 0):
                    _change = self.change(amount - coin)
                    if _change < minChange:
                        minChange = _change
            self.memo[amount] = 1 + minChange
            return self.memo[amount]

    def coinChange(self, coins, amount):
        self.coins = sorted(coins, reverse=True)
        self.memo = {}

        _change = self.change(amount)
        if (_change == float('inf')):
            return -1
        else:
            return _change