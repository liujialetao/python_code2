class Solution:
    def convert(self, s: str, numRows: int) -> str:
        List = ['' for i in range(numRows)]
        select = [i for i in range(numRows)]
        select.extend([i for i in range(numRows - 2, 0, -1)])

        for i in range(len(s)):
            List[select[i % len(select)]] = List[select[i % len(select)]] + s[i]

        ll = ''
        for i in List:
            ll += i
        return ll
s = "PAYPALISHIRING"
numRows = 3
ll = Solution().convert(s, numRows)
ll = Solution().convert(s, numRows)