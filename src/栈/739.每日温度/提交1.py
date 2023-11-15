# 一眼暴力会超时，考虑从后往前比较，最后一天的结果一定是0
# 倒数第二天若温度比最后一天高，则为0，否则为1
# 以此类推，第i天与第i+1天比较
# 比他小，res[i] = 1
# 比他大，
# 如果res[i+1] = 0: res[i] = 0
# 如果res[i+1] != 0: 则根据其res[i+1]的值找到下一天进行反复比较，直到找到比这天温度高的或遍历结束都没有更高的温度
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
            if temperatures[i] >= temperatures[i+1]:
                if res[i+1] == 0:
                    res[i] = 0
                # 后面有比他大的
                elif res[i+1] != 0:
                    j = i+1
                    while j < n:
                        # 如果这天温度比j+res[j]这天的低
                        if temperatures[i] < temperatures[j+res[j]]:
                            res[i] = res[j] + j-i
                            break
                        else:
                            j += res[j]
                            if res[j] == 0:
                                break
        return res
