"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/
"""


import heapq as hq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        idle = {}
        frequency = []

        answer = 1
        for task in tasks:
             hq.heappush(frequency, (-frequency.get(task, 1), task))
             idle[task] = n

        while len(frequency):
            hq.heappop(frequency)
            answer += 1
        
        return answer - 1
            
print(Solution().leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
