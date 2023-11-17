# 考虑前i个字符串匹配前j个字符串的最小操作
# 插入操作dfs(i,j) = dfs(i,j-1) + 1 例horse末尾插入s，与ros末尾匹配，则s抵消掉，转变为horse匹配ro，即dfs(i,j-1)
# 删除操作dfs(i,j) = dfs(i-1,j) + 1 例horse删除e，转变为hors匹配ros,即dfs(i-1,j)
# 替换操作dfs(i,j) = dfs(i-1,j-1) + 1 例 horse末尾替换为s，与ros末尾s抵消，转变为hors匹配ro，即dfs(i-1,j-1)
# 如果s[i] == t[j]，不进行操作，递归到dfs(i-1,j-1)
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def dfs(i, j):
            # 插入j个字符
            if i < 0:
                return j + 1
            # 删除多余的i个字符
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i, j - 1), dfs(i - 1, j), dfs(i - 1, j - 1)) + 1

        return dfs(n - 1, m - 1)
