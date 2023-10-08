"""
2101. Detonate the Maximum Bombs
https://leetcode.com/problems/detonate-the-maximum-bombs/
"""


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        def is_detonated(coor1: tuple[int, int], coor2: tuple[int, int], radius: int):
            (x1, y1), (x2, y2) = coor1, coor2
            return ((x1-x2)**2 + (y1-y2)**2) <= radius**2
        
        
        bombs.sort(key=lambda x: x[0])

        graph = [[] for _ in range(len(bombs))]

        for i, (x, y, r) in enumerate(bombs):
            left, right = i-1, i+1

            while left >= 0:
                _x, _y, _r = bombs[left]
                if x - _x > r:
                    break

                if is_detonated((x, y), (_x, _y), r):
                    graph[i].append(left)
                left -= 1

            while right < len(bombs):
                _x, _y, _r = bombs[right]
                if _x - x > r:
                    break

                if is_detonated((x, y), (_x, _y), r):
                    graph[i].append(right)
                right += 1

        def dfs(graph, visited, i, cnt):

            for _i in graph[i]:
                if visited[_i]:
                    continue
                cnt += 1
                visited[_i] = True
                cnt = dfs(graph, visited, _i, cnt)
            return cnt
        
        answer = 0
        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            visited[i] = True
            cnt = dfs(graph, visited, i, 1)
            if answer < cnt:
                answer = cnt

        return answer


print(Solution().maximumDetonation([[63,47,3],[94,76,1],[38,53,5],[66,67,9],[35,64,10],[43,46,1],[76,95,9],[62,94,3],[42,67,7],[19,84,7],[80,16,9],[7,81,4],[67,25,5],[32,27,1],[2,32,10],[17,46,6],[40,32,6]]))