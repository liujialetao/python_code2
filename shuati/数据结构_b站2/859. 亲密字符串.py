from typing import List

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        def has_twosame(s):
            len
        if len(s)!=len(goal):
            return False
        else:
            n = len(s)
            different_count = 0
            s_=[]
            goal_=[]
            for i in range(n):
                if s[i]!=goal[i]:
                    different_count+=1
                    s_.append(s[i])
                    goal_.append(goal[i])
                    if different_count>2:
                        return False
            if different_count==1:
                return False
            if different_count==2:
                if s_[0]==goal_[1] and s_[1]==goal_[0]:
                    return True
                else:
                    return False
            if different_count==0:
                if len(s)==1:
                    return False
                else:
                    if len(s)!=2 and len(s)!=len(set(s)):
                        return True
                    else:
                        if s[0]==s[1]:
                            return True
                        else:
                            return False

s = "a"

goal = "a"
m = Solution().buddyStrings(s, goal)
pass