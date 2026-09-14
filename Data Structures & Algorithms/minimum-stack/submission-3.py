class MinStack:
    def __init__(self):
        self.stack = []       # stores all values
        self.min_stack = []   # stores the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If min_stack is empty OR val is <= current minimum,
        # save val as a new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the value being removed is also the current minimum,
        # remove it from min_stack too
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        # Last value in normal stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Last value in min_stack is always the current minimum
        return self.min_stack[-1]
'''
Create:
    normal stack
    minimum stack

push(value):
    add value to normal stack
    if value <= current minimum:
        add value to minimum stack

pop():
    if top value == current minimum:
        remove minimum too
    remove top from normal stack

top():
    return top of normal stack

getMin():
    return top of minimum stack
'''
