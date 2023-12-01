class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        # 用哈希表存储每个元素对应的位置信息
        def find_element_positions(matrix):
            element_positions = {}
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    element_positions[matrix[i][j]] = (i, j)
            return element_positions

        element_positions = find_element_positions(mat)
        row_hash, column_hash = {}, {}
        for i in range(len(arr)):
            # 读取元素位置信息
            row, col = element_positions.get(arr[i], (-1, -1))
            if row != -1:
                # 对应行列值+1，如果该行/列的值与矩阵列/行值相等，说明该行/列均已被涂色
                row_hash[row] = row_hash.get(row, 0) + 1
                if row_hash[row] == len(mat[0]):
                    return i
            if col != -1:
                column_hash[col] = column_hash.get(col, 0) + 1
                if column_hash[col] == len(mat):
                    return i
        return -1


instance = Solution()
arr = [1, 4, 5, 2, 6, 3]
matrix = [[4, 3, 5], [1, 2, 6]]
print(instance.firstCompleteIndex(arr, matrix))
