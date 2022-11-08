# -*- coding: utf-8 -*-
# @Time    : 2022/10/9 22:23
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化矩阵
        matrix = [ [0]*n for _ in range(m)]
        # dp = [[1]*n +[[1]+[0]*(n-1) for _ in range(m-1)]]
        #第一行和第一列赋值为1
        for i in range(m):
            matrix[i][0]=1
        for i in range(n):
            matrix[0][i] = 1

        #一行一行给矩阵计算元素值
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] +=cur[j-1]
            for i_ in cur:
                print(i_, end= ' ')
            print()

        return cur[-1]
m,n = 3,7
res = Solution().uniquePaths2(m, n)
pass