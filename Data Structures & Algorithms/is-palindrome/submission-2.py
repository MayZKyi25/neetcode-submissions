class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  s = "Was it a car or a cat I saw????" # for edge cases like this, we'll need a loop (think abt it)
               #^                         ^
         
               #l                         r 

        # need to ignore non alpha numeric -> .isalnum()
        # 2 pointers from left to right to check if each char from l and r is the same
        # if it's not the same, we'll return False
        # else, keep checking until left < right


        # pseudo
        # initialize our left pointer = 0 
        # right pointer = len (s) - 1

        # while left < right: 
            # when each char from left is non alpha numeric (meaning if we see "?" or " empty space")
            # (need a loop to check --> while s[l] is non alpha )
                # increment left +1

            # when each char from right pointer is non alnum, (?)
                # decrement right -1

                # if s[left] is the same as s [right]
                    #left +1
                    #right -1
        # return True (valid palindrome)


        l = 0 
        r = len(s) - 1

        while l < r: 
            while l < r and not s[l].isalnum(): 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1 
            r -=1 
                
        return True







        