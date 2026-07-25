class MinStack:

    def __init__(self):
        self.stack = []
        self.f = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.f) == 0 or val <= self.stack[self.f[-1]]:
            self.f.append(len(self.stack)-1)
        else:
            self.f.appendleft(len(self.stack)-1)

    def pop(self) -> None:
        index = len(self.stack) - 1
        val = self.stack.pop()
        if index == self.f[-1]:
            self.f.pop()
            while len(self.f) > 0 and self.f[-1] > len(self.stack) - 1:
                self.f.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.f[-1]]
