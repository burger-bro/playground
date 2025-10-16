class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""


num = 9669
s = str(num)
s = s.replace("6", "9", 1)
print(s)

