"""
2746. Decremental String Concatenation
https://leetcode.com/problems/decremental-string-concatenation/
"""


class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        def calc(index: int, start: str, last: str) -> int:
            if index == len(words):
                return 0

            tmp, next_index = 1000 * 50 + 1, index + 1

            if words[index][-1] == start:
                tmp = min(tmp, calc(next_index, words[index][0], last) + len(words[index]) - 1)
            else:
                tmp = min(tmp, calc(next_index, words[index][0], last) + len(words[index]))

            
            if words[index][0] == last:
                tmp = min(tmp, calc(next_index, start, words[index][-1]) + len(words[index]) - 1)
            else:
                tmp = min(tmp, calc(next_index, start, words[index][-1]) + len(words[index]))


            return tmp


        return calc(index=1, start=words[0][0], last=words[0][-1]) + len(words[0])
    
print(Solution().minimizeConcatenatedLength(words=["aa","ab","bc"]))
