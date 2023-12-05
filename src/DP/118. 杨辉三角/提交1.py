# f[i][j] = f[i-1][j]+f[i-1][j+1]
# if j = 0 || j = i   f[i][j] = 1
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        ans = []
        for i in range(1, numRows + 1):
            Rows = [1] * i
            for j in range(i):
                if j != 0 and j != i - 1:
                    Rows[j] = ans[i - 2][j - 1] + ans[i - 2][j]
            ans.append(Rows)
        return ans


instance = Solution()
print(instance.generate(5))
