# 改进：函数内嵌，减少调用的开销
# 使用数组存储涂色行列： 由于只需要知道行或列是否被涂色，使用数组而不是字典来存储涂色的行和列可能更为简洁。这样可以省略了对值的维护

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # 用集合存储涂色的行或列
        painted_rows, painted_columns = [0] * m, [0] * n
        element_positions = {}
        for i in range(m):
            for j in range(n):
                element_positions[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            # 读取元素位置信息
            row, col = element_positions.get(arr[i], (-1, -1))
            if row != -1:
                # 对应行列值+1，如果该行/列的值与矩阵列/行值相等，说明该行/列均已被涂色
                painted_rows[row] += 1
                if painted_rows[row] == n:
                    return i
            if col != -1:
                painted_columns[col] += 1
                if painted_columns[col] == m:
                    return i
        return -1


instance = Solution()
arr = [1, 4, 5, 2, 6, 3]
matrix = [[4, 3, 5], [1, 2, 6]]
print(instance.firstCompleteIndex(arr, matrix))
