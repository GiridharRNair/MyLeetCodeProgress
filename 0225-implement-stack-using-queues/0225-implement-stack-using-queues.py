class MyStack:

    def __init__(self):
        self.queue = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        return self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.temp.append(self.queue.popleft())
        out = self.queue.popleft()
        while self.temp:
            self.queue.append(self.temp.popleft())
        return out
    
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()