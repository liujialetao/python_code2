#!/usr/bin/env python
# coding=utf-8

from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = x
        if xx < 0:
            return False

        y = 0
        while (xx // 10 != 0):
            y = y * 10 + xx % 10
            xx = xx // 10
        y = y * 10 + xx
        return x == y


Solution().isPalindrome(1234)
pass



