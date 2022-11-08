from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        a = [[i,j, j-i, height[i], height[j], area]]
        for i in range(n):
            h1 = height[i]
            for j in range(i + 1, n):
                h2 = height[j]
                if temp_area > area:
                    area = temp_area
                    a.append([i,j, j-i, height[i], height[j], area])

    def maxArea2(self, height: List[int]) -> int:
        def cal_area(i, j, height):
            area = (j - i) * min(height[i], height[j])
            return area
        i=0
        j=len(height)-1
        area = cal_area(i, j, height)
        a = [[i,j, '宽度:',j-i, '高度1：', height[i], '高度2：', height[j], '面积：', area]]
        while(i<j):
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            temp_area = cal_area(i, j, height)
            if temp_area>area:
                area = temp_area
                a.append([i,j, '宽度:',j-i, '高度1：', height[i], '高度2：', height[j], '面积：', area])
        return area,a



        return area,a
height = [2,3,10,5,7,8,9]#[1,2,4,3]#[1,8,6,2,5,4,8,3,7]
m = Solution().maxArea2(height)
pass