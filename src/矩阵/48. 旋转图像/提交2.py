# int(n/2) 可写为n // 2, //是整除的意思
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        if n <= 1:
            return
        for j in range(n // 2):
            for i in range(n - 1 - j * 2):
                # 多重赋值简化代码
                matrix[j][i + j], matrix[i + j][n - 1 - j], matrix[n - 1 - j][n - 1 - i - j], matrix[n - 1 - i - j][j] = \
                    matrix[n - 1 - i - j][j], matrix[j][i + j], matrix[i + j][n - 1 - j], matrix[n - 1 - j][
                        n - 1 - i - j]
