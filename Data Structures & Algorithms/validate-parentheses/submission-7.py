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




 
                
                    
            

                
            
            # loop through each bracket, 
            # rule of if it's starting with close paren

            # open paren, save it in stack
            # close paren, pop from open paren stack, check if current has valid pair
            


        

        #   (   [   {   }   ]   )































        # our stack will hold each open paren, and when we see a close paren, we started to pop and see if any open paren match that close paren 
        # rule out if it starts with close paren, it's not valid 






        