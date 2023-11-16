# 考虑第i,j个字符选不选
# 如果s[i] = t[j]，i,j都选，递归到s[i-1],t[j-1] + 1
# 否则选择不选择i或不选择j中长度较大的那个
# i, j都不选的情况被包含在不选i或不选j的下一步递归中
# def dfs(i, j):
#     if i < 0 or j < 0:
#         return 0
#     if text1[i] == text2[j]:
#         return dfs(i - 1, j - 1) + 1
#     return max(dfs(i - 1, j), dfs(i, j - 1))
# return dfs(n - 1, m - 1)
# 翻译为DP：
# f[i][j] = max(f[i-1][j],f[i][j-1])
# f[i+1][j+1] = max(f[i][j+1],f[i+1][j])


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        return f[n][m]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    instance = Solution()
    print(instance.longestCommonSubsequence(text1, text2))
