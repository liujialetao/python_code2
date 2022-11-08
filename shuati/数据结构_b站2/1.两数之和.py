class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            findnumber = target-nums[i]
            if findnumber in nums:
                if findnumber != nums[i]:
                    return [i, nums.index(findnumber)]
                else:
                    if nums.count(findnumber)>=2:
                        return [i, nums.index(nums[i], i+1)]

    def twoSum1(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None:
                if j != i:
                    return [i, j]

nums = [3,0,1,3]
target = 6
a = Solution().twoSum(nums, target)
a = Solution().twoSum1(nums, target)
a = Solution().twoSum1(nums, target)