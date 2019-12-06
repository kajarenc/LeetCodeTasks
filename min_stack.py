
class MinStack:
    """https://leetcode.com/problems/min-stack/"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int):
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()
            return top
            

    def top(self):
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]