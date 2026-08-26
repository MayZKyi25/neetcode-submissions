class Solution:
    def isValid(self, s: str) -> bool:
        # create hashmap:
        # closing bracket -> matching opening bracket
        # Input: s = "([{}])"
        stack = []

        valid_pair = {')':'(', ']':'[', '}': '{'}
        for char in s:
            if char not in valid_pair:
                stack.append(char) #push onto stack
            else:
                if not stack or stack[-1] != valid_pair[char]:
                    return False
                stack.pop()
        return not stack  


        # loop through each character in s:

            # if character is an opening bracket:
                # push it onto stack

            # else: character is a closing bracket

                # if stack is empty:
                    # return False

                # if top of stack does NOT match
                # the opening bracket expected by this closing bracket:
                    # return False

                # otherwise:
                    # pop the matching opening bracket from stack

        # after loop:
            # if stack is empty -> True
            # otherwise -> False







        
   