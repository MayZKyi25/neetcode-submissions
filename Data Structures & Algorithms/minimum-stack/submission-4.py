class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1], val) if self.min_stack else val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# we'll have 2 stacks: 
# 1. regular stack --> push pop top 
# 2. min stack --> keep tracks of cur_min_so_far whenever a stack is appended and removed 
        
