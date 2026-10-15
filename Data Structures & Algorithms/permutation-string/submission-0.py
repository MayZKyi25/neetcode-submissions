class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len (s1) > len (s2): 
            return False

        l, r = 0, len(s1) - 1
        s1_counter = Counter(s1)

        while r < len(s2):
            
            s2_counter = Counter(s2[l:r+1])
            if s1_counter == s2_counter:
                return True
            l +=1
            r +=1
        return False

        # init l, r at ends of s1

        # create counter for s1
        #s1_counter = Counter(s1)
    
        # while r < len(s2):
            # create s2_counter for substr of s2 from l to r
            # if s1_counter == s2_counter
                # return True
            # incr l & r
        
        # return False
        