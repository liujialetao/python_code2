#!/usr/bin/env python
# coding=utf-8

from typing import List

class Solution:
    def maxSubArray_dy(self, nums: List[int]) -> int:
        result = nums[0]
        temp_max = 0
        for i in range(len(nums)):
            temp_max += nums[i]
            result = max(result, nums[i], temp_max)
            if temp_max < 0:
                temp_max = 0
        return result

    def maxSubArray(self, nums: List[int]) -> int:
        # print(nums)
        result = nums[0]
        while len(nums)>0:
            if nums[0]<=0:
                result = max(nums[0],result)
                nums.pop(0)
            else:
                break
        while len(nums)>0:
            if nums[-1]<=0:
                nums.pop()
            else:
                break
        #如果全是负数，返回max，此时的nums为空
        if len(nums)==0:
            return result

        # print(nums)
        #将相同符号的数合并为正负正...负正的形式
        new_nums = []
        postive=negtive=0
        flag=1
        for i in range(0, len(nums)):
            if nums[i]>=0:
                if flag==-1:
                    new_nums.append(negtive)
                    negtive=0
                postive+=nums[i]
                flag=1
            else:
                if flag==1:
                    new_nums.append(postive)
                    postive=0
                negtive+=nums[i]
                flag=-1
        new_nums.append(postive)
        # print(new_nums)

        result = new_nums[0]
        temp_max = 0
        for i in range(len((new_nums))//2):
            sum = new_nums[2*i]+new_nums[2*i+1]
            if sum < 0:
                result = max(new_nums[2*i], result, temp_max, temp_max+new_nums[2*i])
                if temp_max+sum>0:
                    temp_max = temp_max+sum
                else:
                    temp_max = 0
            else:
                result = max(result, temp_max + new_nums[2 * i])
                temp_max += sum

        result = max(result,new_nums[-1],temp_max+new_nums[-1])
        return result

    def maxSubArray_baoli(self, nums: List[int]) -> int:
        def f(a):
            sum=0
            for i in a:
                sum+=i
            return sum
        sum=nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum_temp = f(nums[i:j+1])
                if sum_temp > sum:
                    sum = sum_temp
                    ii=i
                    jj=j
                    print(i,j)
        return sum,ii,jj

import random

for j in range(100):
    print(j)
    nums = []
    flag=1
    for i in range(10):
        digit = random.randint(1,8)
        nums.append(flag*digit)
        flag*=-1
    nums.append(10)
    # nums =
    m1 = Solution().maxSubArray(nums)
    m2 = Solution().maxSubArray_baoli(nums)
    x=(m1==m2[0])
    if x!=True:
        print('woca')
pass