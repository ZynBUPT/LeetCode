class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            # 用列表推导式简化
            Rows = [1] + [ans[i - 1][j - 1] + ans[i - 1][j] for j in range(1, i)] + [1]
            ans.append(Rows)
        return ans
