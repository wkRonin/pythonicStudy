"""
给定一个由N个整数组成的数组A，一次移动，我们可以选择此数组中的任何元素并将其替换为任何值。
数组的振幅是数组A中的最大值和最小值之间的差。 返回通过执行最多三次替换之后数组A的最小振幅。
N是一个整数而且范围是: [2, 10000]
A数组中的每一个元素都是整数而且范围是: [-50, 50]
"""


"""
复杂度分析
时间复杂度：O(nlogn)
需要遍历一遍数组，并且排序算法时间复杂度为O(nlogn)。
空间复杂度：O(1)
"""


class Solution:
    """
    @param A: a list of integer
    @return: Return the smallest amplitude
    """

    def MinimumAmplitude(self, A):

        if len(A) <= 4:
            return 0

        length = len(A)
        A = sorted(A)
        mmin = float('inf')

        for i in range(4):
            mmin = min(mmin, A[length - 3 + i - 1] - A[i])
        return mmin


A = [11, 0, -6, -1, -3, 5]
solution = Solution()
print(solution.MinimumAmplitude(A))
