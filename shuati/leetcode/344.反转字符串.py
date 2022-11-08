from typing import List
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         if len(s)==2:
#             return s[1].append(s[0])
#         else:
#             return self.reverseString(s[1:]).append(s[0])
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


s = list('hello')
print(s)
x=Solution().reverseString(s)
print(x)
print(x)