"""
486. Predict the Winner
https://leetcode.com/problems/predict-the-winner/
"""


class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            print("??")
            dp[i] = nums[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
                print(i, j, dp)

        return dp[n-1] >= 0

print(Solution().predictTheWinner([1,5,233,7]))