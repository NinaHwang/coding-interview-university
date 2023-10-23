"""
120. Triangle
https://leetcode.com/problems/triangle/
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
            
        INF = 10**4 + 1
        dp = [triangle[0][0]]
        answer = INF

        i = 1
        for i in range(1, len(triangle)):
            tmp_dp = []
            for j in range(i+1):
                l, r = j - 1, j
                lp, rp = INF, INF
                if l >= 0:
                    lp = dp[l]
                if r < i:
                    rp = dp[r]
                tmp = min(lp, rp) + triangle[i][j]

                if i < len(triangle) - 1:
                    tmp_dp.append(tmp)
                else:
                    if tmp < answer:
                        answer = tmp
            dp = tmp_dp
            
        return answer
    

print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
