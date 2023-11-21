# 动态规划，能做但是超时了，O(n2)隔壁java勉强能通过
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        # 遍历i之前的所有结点
        for i in range(1, n):
            for j in range(i):
                # 如果有能从j直接跳到i的，更新dp[i]
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    instance = Solution()
    print(instance.jump(nums))
