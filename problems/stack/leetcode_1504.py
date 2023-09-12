"""
1504. Count Submatrices With All Ones
https://leetcode.com/problems/count-submatrices-with-all-ones/description/
"""


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat[0]), len(mat)

        # to avoid the worst case scenario: all elements are 1
        flag = True
        for row in mat:
            if sum(row) != m:
                flag = False
        if flag and m > 1 and n > 1:
            return (n * (n+1)// 2) * (m * (m+1)//2)

        def calc(coordinates: tuple[int, int], limit: tuple[int, int]=(m-1, n-1)) -> int:
            initial_x, initial_y = coordinates  # initial starting point
            x, y = coordinates
            _x, _y = limit

            cnt = 1  # it is 1 because it includes the value of the initial starting point will always be 1 (L52)

            while x <= _x and y <= _y:
                if x == _x and y == _y:
                    break

                x += 1  # move 1 to right
                if x <= _x:
                    if mat[y][x]:  # if mat[y][x] is True, add 1 to the cnt, 
                        cnt += 1
                        continue
                    _x = x - 1  # else, set x's limit as x - 1 and set x as its initial value
                    x = initial_x
                else:
                    x = initial_x
                
                y += 1  # move 1 to below
                if y <= _y:
                    if mat[y][x]:
                        cnt += 1
                        continue
                    _y = y - 1
                
            return cnt
        
        answer = 0
        for j in range(n+1):
            for i in range(m+1):
                if mat[j][i]:  # only if the starting point is 1
                    answer += calc((i, j))
        
        return answer
