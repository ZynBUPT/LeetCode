# 字符串要能被除尽，除数的长度必须能被被除数的长度整除
# 满足要求的最长字符串长度即为两字符串长度的最大公因数
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        # 辗转相除法求最大公因数
        while n != 0:
            n, m = m % n, n
        # 取出前m位
        return str1[:m] if str1 + str2 == str2 + str1 else ''