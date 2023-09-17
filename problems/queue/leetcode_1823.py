"""
1823. Find the Winner of the Circular Game
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""


from collections import deque as dq


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = dq(range(1, n+1))

        while q: # n times
            q.rotate(-(k-1))  # O(n)
            popped = q.popleft()  # O(1)
        return popped
