"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        # head's next node will be head's second next node(a -> c) and head's next node will be the new head (b -> a)
        a, b, c = head, head.next, head.next.next
        b.next, a.next = a, c
        head = b

        # x -> y -> z, swap y and z
        x = head.next
        while x.next and x.next.next:
            y, z = x.next, x.next.next
            y.next = z.next  # y -> z.next
            z.next = y  # z -> y
            x.next = z  # x -> z  => x -> z -> y -> z.next
            x = y  # y will be new x (because the position of y is already determined)

        return head
    