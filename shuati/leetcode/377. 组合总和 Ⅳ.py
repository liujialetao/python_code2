# -*- coding: utf-8 -*-
# @Time    : 2022/10/7 19:05
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #存放符合要求的序列
        suc = []
        candidates = []
        for ele in nums:
            tmp = [[ele], ele]
            candidates.append(tmp)

        while candidates!=[]:
            #筛选候选集
            new_candidates = []
            for candidate in candidates:
                if candidate[1]<target:
                    new_candidates.append(candidate)
                if candidate[1]==target:
                    suc.append(tuple(candidate[0]))

            # 制作新的候选集
            candidates = []
            for candidate in new_candidates:
                for num in nums:
                    can = [candidate[0]+[num], candidate[1]+num]
                    candidates.append(can)
            # for ele in candidates:
            #     print(ele)
            # print()
        return len(suc)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                    print(f"i:{i} num:{num} i-num:{i - num} dp:{dp}")

        return dp[target]

res = Solution().combinationSum4(nums = [1,2,3], target = 5)
pass