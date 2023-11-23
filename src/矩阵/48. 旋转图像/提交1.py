# 1,2 → 2，3→ 3，2 →2，1
# 1，3 → 3，4 → 4，2 → 2，1
# 1，2 → 2，4 → 4，3 → 3，1
# 1，1 → 1，4 → 4，4 → 4，1
# 1，i → i，4 → 4，n-i → n-i，1
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        if n <= 1:
            return
        for j in range(int(n / 2)):
            for i in range(n - 1 - j * 2):
                temp = [matrix[j][i + j], matrix[i + j][n - 1 - j], matrix[n - 1 - j][n - 1 - i - j],
                        matrix[n - 1 - i - j][j]]
                matrix[j][i + j] = temp[3]
                matrix[i + j][n - 1 - j] = temp[0]
                matrix[n - 1 - j][n - 1 - i - j] = temp[1]
                matrix[n - 1 - i - j][j] = temp[2]


instance = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
instance.rotate(matrix)
print(matrix)
