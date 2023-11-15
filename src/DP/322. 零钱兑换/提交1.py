"""
def dfs(i,c):
    if i < 0:
        return 0 if c == 0 else inf
    # 如果剩余金额小于硬币数额，则不选择
    if c < coins[i]:
        return dfs(i-1,c)
    # 返回选或不选该硬币的数量的最小值，且同一面额可以反复选择，第二个dfs i的编号不用减一
    return min(dfs(i-1,c), dfs(i,c-coins[i]) + 1)

ans = dfs(n-1,amount)
return ans if ans < inf else -1
"""
# 翻译为递推式
# f[i][c] = min(f[i-1][c],f[i][c-x] + 1)
# f[i+1][c] = min(f[i][c],f[i+1][c-x] + 1)  防止出现负数下标

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        f = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        # 初始值
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    instance = Solution()
    print(instance.coinChange(coins, amount))


