from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        temp_string = s[0]
        max_length = 1
        n = len(s)
        for i in range(1, n):
            if s[i] not in temp_string:
                temp_string += s[i]
            else:
                temp_max_length = len(temp_string)
                if temp_max_length > max_length:
                    max_length = temp_max_length
                pos = temp_string.index(s[i])
                temp_string = temp_string[pos + 1:]+s[i]
        max_length = max(max_length, len(temp_string))
        return max_length
s = "au"
m1 = Solution().lengthOfLongestSubstring(s)