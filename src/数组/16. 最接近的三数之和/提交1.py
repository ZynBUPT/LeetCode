class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closeSum = float('inf')
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                closeSum = current if abs(target - current) < abs(target - closeSum) else closeSum
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
        return closeSum


instance = Solution()
print(instance.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))