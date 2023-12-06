# 有负数的基数排序
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        min_num = min(nums)
        # 所有数平移到非负范围内
        nums = [num - min_num for num in nums]
        max_num = max(nums)
        # 确定最大数的位数
        max_digits = len(str(max_num))
        # 定义0~9的桶
        buckets = [[] for _ in range(10)]
        # 进行最大位数趟排序
        for digit in range(max_digits):
            # 将数组元素放入对应的桶中
            for num in nums:
                # 获取当前位的数字
                radix = (num // (10 ** digit)) % 10
                buckets[radix].append(num)
            nums = []
            for bucket in buckets:
                nums.extend(bucket)
                # 清空每个桶中的元素
                bucket.clear()
        nums = [num + min_num for num in nums]
        return nums

# 给你一个整数数组 nums，请你将该数组升序排列。
