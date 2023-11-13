"""
337. House Robber III
https://leetcode.com/problems/house-robber-iii/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
        
        return dfs(root)

print(
    Solution().rob(
    TreeNode(
        val=3, 
        left=TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None)), 
        right=TreeNode(val=3, left=None, right=TreeNode(val=4, left=None, right=None))
    )
    )
)



            
            

