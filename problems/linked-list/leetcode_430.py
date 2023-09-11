"""
430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node | None) -> Node | None:
        def recurr(head):
            node = head
            while node:
                _next = node.next  # save the next node

                if node.child:
                    node.next, child_tail = recurr(node.child)  # get child's head and tail, set current node's next node as the node of child's head
          
                    node.next.prev = node  # set child's head node's prev node to current node
                    node.child = None  # set child pointer to null
                    
                    child_tail.next = _next  # link child's tail to the saved next node(L18)
                    if child_tail.next:  # only if the saved next node is not null
                        child_tail.next.prev = child_tail  # set the saved next node's prev to the child's tail.
                        node = child_tail  # set current node to child's tail node

                # if node.next is not null, set current node as node.next. Or, return head and the current node as tail right away
                if node.next:
                    node = node.next
                else:
                    break
                
            return head, node

        return recurr(head)[0]


