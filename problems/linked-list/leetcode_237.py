"""
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # current node: the node that should be deleted
        node.val = node.next.val  # set the value of the current node to the value of the next node
        node.next = node.next.next  # link the node to the second next node
