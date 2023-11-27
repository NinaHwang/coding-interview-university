"""
1670. Design Front Middle Back Queue
https://leetcode.com/problems/design-front-middle-back-queue/
"""


class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
        n = len(self.queue) // 2
        self.queue.insert(n, val)
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        

    def popFront(self) -> int:
        if self._can_pop(self.queue):
            return self.queue.pop(0)
        return -1
        

    def popMiddle(self) -> int:
        if self._can_pop(self.queue):
            n = len(self.queue) // 2
            _n = n if len(self.queue) % 2 else n - 1
            return self.queue.pop(_n)
        return -1
        

    def popBack(self) -> int:
        if self._can_pop(self.queue):
            return self.queue.pop()
        
        return -1
    
    def _can_pop(self, q) -> bool:
        if q:
            return True
        return False
        