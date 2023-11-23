#           1  2  3
#           4  5  6  x
#    ------------------
#            6  12  18
#        5  10  15
#    4   8  12
#    ------------------
#    4  13  28  27  18


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        sum = [0] * (m + n)
        res = ''
        for i in range(m):
            for j in range(n):
                sum[i + j] += int(num1[m - i - 1]) * int(num2[n - 1 - j])
        for i in range(len(sum)):
            if sum[i] >= 10:
                sum[i + 1] += sum[i] // 10
                sum[i] %= 10
            res = str(sum[i]) + res
        # 处理最高位是0
        if res[0] == '0':
            res = res.lstrip('0')
        return res if res else '0'


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    instance = Solution()
    print(instance.multiply(num1, num2))
