"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                ans.append("")
                continue
            elif c == ")":
                if stack:
                    j = stack.pop()
                    ans[j] = "("
                    ans.append(c)
                else:
                    ans.append("")
            else:
                ans.append(c)
        return "".join(ans)
    
print(Solution().minRemoveToMakeValid(s = "a)b(c)d"))
        