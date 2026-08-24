class Solution:
    def isPalindrome(self, s: str) -> bool:



        '''
        "W!!!!!!as it a car or a cat I saw????"
        l                                  r   
        wasitacar o racatisaw    
                l   r 

        '''

        left = 0 
        right = len(s) - 1

        while left < right: 
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum(): 
                right -=1                
            if s[left].lower() != s[right].lower(): 
                return False
            # moving to the middle 
            left += 1
            right -= 1
        return True


        # left = 0 (left starts at 0)
        # right = length of the string - 1 (right starts at end of the string)

        # while left < right:   

            # check if each char from left is not alphanum

            # check if each char from right is not alphanum()

                # if so, compare them if they're the same, contiue the while loop 
                    # move the left and right pointer towards each other 
                # else: 
                    #Flase
        # return True
        