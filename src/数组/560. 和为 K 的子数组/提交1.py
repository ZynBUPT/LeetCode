# sum(i,j) = sum(0,j) - sum(0,i)
# pre(i) = pre(i-1) + num[i]
# 求子数组和=k
# 即pre(i) - pre(j-1) == k
# pre(j-1) == pre(i) - k    →   统计有多少个pre(j)和为pre(i)-k
# 将pre(j)用哈希表储存
# 每前进一步计算pre - k， 答案加上hashmap(pre-k)的值

# 后面的前缀和-前面的前缀和==k 那么中间的哪些值必然就是可以组成的子数组
# 维护个数是因为 可能会有多个x(x==后面的前缀和-前面的前缀和) 所以我们需要边遍历边+维护的个数
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans, pre = 0, 0
        # 初始化，和为0有1种方法
        hashmap = {0: 1}
        for num in nums:
            # 计算pre(i)
            pre += num
            if pre - k in hashmap:
                ans += hashmap[pre - k]
            hashmap[pre] = hashmap.get(pre, 0) + 1
        return ans


if __name__ == '__main__':
    instance = Solution()
    nums = [1, 2, 3]
    print(instance.subarraySum(nums, 3))
