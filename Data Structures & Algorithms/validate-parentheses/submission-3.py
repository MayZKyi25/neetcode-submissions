class Solution:
    def isValid(self, s: str) -> bool:

        # Opening bracket → push it onto the stack

        # Closing bracket →
        #     Is the stack empty? Invalid
        #     Does the top opening bracket not match? Invalid
        #     Otherwise, remove the matching opening bracket

        # After the loop →
        #     Empty stack = valid
        #     Anything remaining = invalid

        my_stack = []
        valid_paren_pair = {')': '(', '}': '{', ']': '['}
        
        for i in range(len(s)):
            if s[i] not in valid_paren_pair: 
                my_stack.append(s[i])
            else:
                if not my_stack or my_stack[-1] != valid_paren_pair[s[i]]:
                    return False

                my_stack.pop()
        return not my_stack

        # my error log: 

        # for i in range(len(s)):
        #     if s[i] == valid_paren_pair.values():
        #         return false
        #     my_stack.append(s[i])
        #     if my_stack[i] in valid_paren_pair: 
        #         my_stack.pop(s[i])


      
        