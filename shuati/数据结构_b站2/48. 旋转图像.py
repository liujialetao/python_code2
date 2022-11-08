from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #计算图像的宽度
        length=len(matrix)
        #计算外循环的次数
        n = length//2
        for i in range(n):
            #内循环交换的次数这个区间为四边形宽度所在地方
            for j in range(i,length-i-1):
                print(matrix[i][j], matrix[j][length-i-1],\
                      matrix[length-i-1][length-i-1-i], matrix[length-i-1-j][i])
                # temp=matrix[length-i-1-j][i]
                # matrix[length - i - 1 - j][i]=matrix[length-i-1][length-i-1-j]
                # matrix[length - i - 1][length - i - 1 - j]=matrix[j][length-i-1]
                # matrix[j][length - i - 1]=matrix[i][j]
                # matrix[i][j]=temp
        return matrix
import numpy as np
n=5
matrix=np.arange(n*n).reshape((n,n)).tolist()
def ppint(matrix):
    for i in matrix:
        print(i)
ppint(matrix)
Solution().rotate(matrix)
print('\n')
ppint(matrix)




