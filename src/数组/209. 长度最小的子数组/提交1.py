# 双指针，当右边移动到子数组和大于k时，向右移动左指针缩小数组长度直到数组和小于k
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        n = len((nums))
        sum = 0
        left = 0
        for right in range(n):
            sum += nums[right]
            while sum >= target:
                length = right - left + 1
                res = min(length, res)
                sum -= nums[left]
                left += 1
        return res if res < float('inf') else 0
