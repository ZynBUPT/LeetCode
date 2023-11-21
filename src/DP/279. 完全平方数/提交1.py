import math


class Solution:
    def numSquares(self, n: int) -> int:
        num = int(math.sqrt(n))
        if num * num == n:
            return 1
        choice = [x * x for x in range(1, num + 1)]
        f = [[float('inf')] * (n + 1) for _ in range(num + 2)]
        f[0][0] = 0
        for i, x in enumerate(choice):
            for c in range(n + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[num][n]
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    n = 13
    instance = Solution()
    print(instance.numSquares(n))
