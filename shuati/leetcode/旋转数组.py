from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n=len(numbers)
        x1=1
        x2=n-1
        if x2>=numbers[0]:
            return numbers[0]
        while(x2-x1>1):
            if numbers[(x1+x2)//2]>=numbers[x2]:
                x1=(x1+x2)//2
            else:
                x2 = (x1 + x2) // 2
        return numbers[x2]

numbers=[2,2,2,0,1]
x=Solution().minArray(numbers)
print(x)
print(x)