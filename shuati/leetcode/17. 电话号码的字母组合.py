from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {'2':'abc',  '3':'def', '4': 'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        for i in digits:
            res.append(list(dictionary[i]))
        ress=['']
        while(res):
            now=res.pop(0)
            new=[]
            for i in ress:
                for j in now:
                    new.append(i+j)
            ress=new
        return ress



digits = '23456789'
ress=Solution().letterCombinations(digits)
print(ress)
print(ress)


