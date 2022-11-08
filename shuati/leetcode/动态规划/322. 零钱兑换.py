# -*- coding: utf-8 -*-
# @Time    : 2022/10/9 23:07
from typing import  List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if 1 in coins:
            max_value = max(coins)
            res = amount//max_value + amount%max_value
            return res
        else:
            def digui(coins, amount):
                if amount<0:
                    return 10000

                if amount==0:
                    return 0

                if amount>0:
                    a = []
                    for coin in coins:
                        remain_amount = amount-coin
                        if remain_amount not in all_ready_treated:
                            b = digui(coins, remain_amount)
                            all_ready_treated[remain_amount]=b
                        else:
                            b = all_ready_treated[remain_amount]
                        a.append(b)

                    res = min(a) + 1
                    # print(res)
                    return res

            all_ready_treated = {}
            min_res = digui(coins, amount)
            if min_res>10000:
                return -1
            return min_res




    def coinChange2(self, coins: List[int], amount: int) -> int:
        if (len(coins) == 0):
            return -1
        dp = [(amount + 1) for i in range(amount + 1)]
        dp[0] = 0
        for m in range(amount + 1):
            for n in range(len(coins)):  # len(coins)
                if (coins[n] <= m):
                    dp[m] = min(dp[m],
                                dp[m - coins[n]] + 1)  # 有可能前面的是不可能凑齐的零钱数 这样dp[m-coins[n]] + 1 会大于dp[m]
                print(dp[m], dp[m - coins[n]] + 1)
                print(dp)
        return -1 if dp[amount] > amount else dp[amount]

res = Solution().coinChange2(coins = [1, 3, 5], amount = 6)
print(res)