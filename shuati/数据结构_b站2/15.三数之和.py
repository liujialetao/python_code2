class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        ans = []

        print(nums)
        # 小于3个元素
        if length < 3:
            return []
        # 最小的数大于0
        if nums[0] > 0:
            return []
        for k in range(length - 2):
            if nums[k] > 0:
                break
            i, j = k + 1, length - 1
            if k > 0 and nums[k] == nums[k - 1]: continue

            while (i < j):
                s = nums[k] + nums[i] + nums[j]

                if s == 0:
                    single_list = [nums[k], nums[i], nums[j]]
                    ans.append(single_list)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j + 1] == nums[j]: j -= 1

                elif s > 0:
                    j -= 1
                    while i < j and nums[j + 1] == nums[j]: j -= 1

                else:
                    i += 1
                    while i < j and nums[i - 1] == nums[i]: i += 1

        return ans
ans = Solution().threeSum([-2,-8,2,8,5,6])
print(ans)
print(ans)