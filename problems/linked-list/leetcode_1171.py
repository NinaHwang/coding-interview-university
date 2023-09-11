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
        
        while head and head.val == 0:  # Ignore the first zeros
            head = head.next
        prev_node, node = IS_HEAD, head  # Zeros were removed, current node is the head

        while node:
            if node.val == 0:  # If current node's value is 0, 
                if prev_node != True:  # If current node is not the head, link the previous node and the next one
                    prev_node.next = node.next
                else:  # If current node is the head, the next node will be the new head
                    head = node.next
                node = node.next
                continue
            
            if saved_node := _dict.get(-node.val):  # If current value can make zero sum,
                if saved_node == True:  # If current node is the head, the next node will be the new head
                    head = node.next
                else:  # If current node is not the head, link the last node after the node that makes the zero sum is removed to the next node of the current node
                    saved_node.next = node.next
                
                # initialize _dict and prev_node. set current node as new head
                _dict = {}
                prev_node, node = IS_HEAD, head
                continue

            # If current value cannot make zero sum,
            new_dict = {k+node.val: v for k, v in _dict.items()}  # modify _dict
            if new_dict.get(node.val, False) == False:  # if current value does not exist in new_dict, add as a new case
                new_dict[node.val] = prev_node
            _dict = new_dict
            
            prev_node = node
            node = node.next

        return head
    