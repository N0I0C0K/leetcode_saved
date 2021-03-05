class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.res.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        r = self.res.pop(0)
        return r

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.res) >= 1:
            r = self.res[0]
            return r
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.res) > 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()