# 可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。
# 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。
# 单调栈满足从栈底到栈顶元素对应的温度递减，因此每次有元素进栈时，
# 会将温度更低的元素全部移除，并更新出栈元素对应的等待天数，这样可以确保等待天数一定是最小的。
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            # 栈不空，比较栈顶元素对应的温度和当前温度
            # 如果小于当前温度，则移除，直到大于当前温度或排空栈，然后将i入栈
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
