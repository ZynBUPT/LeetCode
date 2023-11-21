class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        maxPos = 0  # 目前能到达的最远位置，即前i个能到达的最远位置
        border = 0  # 上次跳跃可达右边的范围边界，也是下次能作为起跳点最右的位置
        step = 0
        for i in range(n-1):
            maxPos = max(maxPos, nums[i] + i)
            # 到达边界后取最远位置贪心
            if i == border:
                border = maxPos
                step += 1
        return step
