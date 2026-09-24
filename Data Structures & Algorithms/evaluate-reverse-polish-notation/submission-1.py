class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        mystack = [] 

        # For tokens = ["8", "2", "/"]:

        # For "8" → save 8: stack = [8]
        # For "2" → save 2: stack = [8, 2]
        # For "/" → take out both numbers, divide, and save the result: stack = [4]


        for i in tokens:
            if i == "+":
                mystack.append(mystack.pop() + mystack.pop()) 
            elif i == "-":
                a, b = mystack.pop(), mystack.pop()
                mystack.append(b-a)
            elif i == "*": 
                mystack.append(mystack.pop() * mystack.pop())
            elif i == "/":
                a, b = mystack.pop(), mystack.pop() 
                mystack.append(int(b/a))
            else: 
                mystack.append(int(i))
        return mystack[0]