"""
1171. Remove Zero Sum Consecutive Nodes from Linked List
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    !! Not so optimal time complexity - need to review
    """
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        _dict = {}
        IS_HEAD = True
        
        while head and head.val == 0:
            head = head.next
        prev_node, node = IS_HEAD, head

        while node:
            if node.val == 0:
                if prev_node != True:
                    prev_node.next = node.next
                else:
                    head = node.next
                node = node.next
                continue
            
            if saved_node := _dict.get(-node.val):
                if saved_node == True:
                    head = node.next
                else:
                    saved_node.next = node.next
                
                _dict = {}
                prev_node, node = IS_HEAD, head
                continue

            new_dict = {k+node.val: v for k, v in _dict.items()}
            if new_dict.get(node.val, False) == False:
                new_dict[node.val] = prev_node
            _dict = new_dict
            
            prev_node = node
            node = node.next

        return head
    