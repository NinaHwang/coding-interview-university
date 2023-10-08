"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.idx = 0

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {v : i for i, v in enumerate(inorder)}
        
        def recursive(l: int, r: int) -> TreeNode | None:
            if l > r: 
                return
            
            node = TreeNode(val=preorder[self.idx])
            
            i = inorder_map[node.val]
            self.idx += 1

            node.left = recursive(l, i-1, self.idx)
            node.right = recursive(i+1, r, self.idx)
            
            return node
        
        return recursive(0, len(inorder)-1)

    

print(Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
