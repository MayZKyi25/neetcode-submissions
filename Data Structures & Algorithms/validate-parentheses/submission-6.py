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
            if current not in close_to_open: # meaning start with open brackets, add to stack
                my_stack.append(current)
            else: 
                if not my_stack or my_stack.pop() != close_to_open[current]: 
                    return False
        return not my_stack 
                
                    
            

                
            
        print (my_stack)
            
            # rule out if it's start with close paren 
            # if it's open paren, we store in stack
            # if it's close paren, we pop it and see if there's a correct valid_paren
            


        

        #   (   [   {   }   ]   )































        # our stack will hold each open paren, and when we see a close paren, we started to pop and see if any open paren match that close paren 
        # rule out if it starts with close paren, it's not valid 






        