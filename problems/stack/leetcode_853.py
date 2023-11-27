"""
853. Car Fleet
https://leetcode.com/problems/car-fleet/
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, key = lambda x: x[0])

        times = [(target - (position := car[0]))/(speed := car[1]) for car in cars]

        stack = []
        for time in times:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time) 
        return len(stack)


print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))