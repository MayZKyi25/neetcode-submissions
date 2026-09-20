class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = { 
        ')':'(',
        '}':'{',
        ']':'[' 
        }
        my_stack = [] 

        for bracket in range(len(s)): 
            current = s[bracket]
            # if it doesnt' start with closing bracket, save it in our stack
            if current not in close_to_open: 
                my_stack.append(current)

            # else handles closing brackets, pop my_stack and check if there's valid pair
            else: 
                # if open bracket '(' not the same as it's closing bracket ')' 
                if not my_stack or my_stack.pop() != close_to_open[current]:
                    return False
        return not my_stack 

        # If the current bracket is an opening bracket,
        # save it in the stack.
            # Otherwise, the current bracket is a closing bracket.
            # Invalid if:
            # 1. There is no opening bracket in the stack, OR
            # 2. The most recent opening bracket does not match
            #    the current closing bracket.
            #
            # Example: if current is "}",
            # close_to_open[current] gives us "{".

    # The string is valid only if no unmatched opening brackets remain.


    '''
        Create a map that connects each closing bracket to its matching opening bracket
        Create an empty stack

        For each bracket in the string:

            If it is an opening bracket:
                Add it to the stack

            Otherwise, it is a closing bracket:

                If the stack is empty:
                    Return False

                Remove the most recent opening bracket from the stack

                If that opening bracket does not match
                the current closing bracket:
                    Return False

        After checking every bracket:

            If the stack is empty:
                Return True

            Otherwise:
                Return False
                

    Valid Parentheses — Error Log
    - Compared closing bracket directly with opening bracket.
    - Forgot to use close_to_open[current] to get the required opening bracket.
    - Called .pop() without first checking whether the stack was empty.
    - Final check should be return not my_stack, not return my_stack.
'''       