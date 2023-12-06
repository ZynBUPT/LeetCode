#   1  2  3  4  5  6
#   7  8  9 10 11 12
#  13 14 15 16 17 18
#  19 20 21 22 23 24
#  25 26 27 28 29 30
# 矩阵遍历方向→↓←↑作为一次循环，然后以同样方法遍历子矩阵
# 先实现一圈的遍历，再根据特征遍历子矩阵
import math


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while left <= right and top <= bottom:
            # 从左到右
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1
            # 从上到下
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            # 从右到左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


matrix = [[1, 2, 3, 4]]
instance = Solution()
print(instance.spiralOrder(matrix))
