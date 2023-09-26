"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from enum import Enum


class OperatorEnum(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def calc(operator: OperatorEnum, a: int, b: int):
            match operator:
                case OperatorEnum.PLUS.value:
                    return a + b
                case OperatorEnum.MINUS.value:
                    return a - b
                case OperatorEnum.MULTIPLY.value:
                    return a * b
                case OperatorEnum.DIVIDE.value:
                    return int(a / b)
                case _:
                    raise ValueError

        nums = []
        
        for i in tokens:
            try:
                i = int(i)
                nums.append(i)
            except ValueError:
                b = nums.pop()
                a = nums.pop()
                nums.append(calc(i, a, b))
        print(nums)
        return nums[0]
    

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


      