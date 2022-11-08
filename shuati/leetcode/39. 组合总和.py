# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 11:03
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
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
                    candidate[0].sort()
                    suc.append(candidate[0])

            # 制作新的候选集
            candidates = []
            for candidate in new_candidates:
                for num in nums:
                    can = [candidate[0]+[num], candidate[1]+num]
                    candidates.append(can)
            # for ele in candidates:
            #     print(ele)
            # print()
        res = []
        for ele in suc:
            if ele not in res:
                res.append(ele)
        return res


nums = [2,22,4,17,28]
target = 30
res = Solution().combinationSum(nums = nums, target =target )
pass