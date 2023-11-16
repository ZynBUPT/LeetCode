class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(nums, path):
            if not nums:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        return ans
