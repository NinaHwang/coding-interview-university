"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        answer = 1
        dq = deque([nums[0]])
        _max, _min = nums[0], nums[0]

        for n in nums[1:]:
            if n > _max:
                _max = n
            elif n < _min:
                _min = n
            
            dq.append(n)
            answer += 1

            if _max - _min > limit:  # if max - min is greater than limit, slide the window to the right
                answer -= 1
                popped = dq.popleft()
                if popped == _max:
                    _max = max(dq)
                elif popped == _min:
                    _min = min(dq)

        return answer


print(Solution().longestSubarray(nums = [4,8,5,1,7,9], limit = 6))
print(Solution().longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
print(Solution().longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))
