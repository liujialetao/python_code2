# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 19:15

from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(lst, nums):
            # 递归结束条件
            if nums == []:
                res.append(lst[:])
                return

            for i in range(len(nums)):
                ele = nums[i]
                remain_nums = nums[:i]+nums[i+1:]
                lst.append(ele)
                dfs(lst, remain_nums)
                #还原列表，进行下个元素的计算
                lst.pop()

        res = []
        dfs([],nums)

        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res




nums = [1,2,3]
res = Solution().permute1(nums=nums)
# res = Solution().permute_1(nums=nums)
pass