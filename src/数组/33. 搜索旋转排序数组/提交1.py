# 二分查找后，其中一个子数组是有序的，另一个可能有序，可能部分有序
# 递归查找，判断在有序还是无序部分进行查找
# 4 5 6 7 |8| 9 0 1 2 target = 1
# 7 8 9 0 |1| 2 4 5 6 target = 9
# 特殊情况：旋转后还是有序序列
# 1 2 3 4 |5| 6 7 8 9 target = 7
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # 如果nums[mid]大于等于nums[left]，说明左半部分是有序的
                # 此时若target大于nums[left]又小于nums[mid]的话，在左半部分查找，否则在右半部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 同上
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


nums = [4, 5, 6, 7, 8, 9, 0, 1, 2]
target = 9
instance = Solution()
print(instance.search(nums, target))

# 整数数组nums按升序排列，数组中的值互不相同。在传递给函数之前，nums在预先未知的某个下标k（0 <= k < nums.length）上进行了旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如，[0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你旋转后的数组nums和一个整数target，如果nums中存在这个目标值target，则返回它的下标，否则返回 -1 。
# 你必须设计一个时间复杂度为O(log n)的算法解决此问题。
