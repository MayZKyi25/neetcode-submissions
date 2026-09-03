class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    # x   y   a   j   i   e   w   m   k   g   o   j   z   i   a
    #     l                                           r
                                             
        # init set for letters
        # init valid_window = 0 
        # l = 0 

        # for r in length s: 
            # while s[r] duplicate is found: 
                # remove l[r] from the hashset
                # increase l by 1
            # add s [r] to our set 
            # valid_window =  max (valid_window, (r-l)+1)
        # return valid_window

        str_set = set()
        valid_window = 0 
        l = 0 

        for r in range(len(s)):
            while s[r] in str_set:
                str_set.remove(s[l])
                l += 1
            str_set.add(s[r])
            valid_window = max(valid_window, (r-l)+1)
        return valid_window






    



































    #        z x y c b a y d e x a z # answer is 7
    #        l
    #                     r


        # init set
        # init max_len

        # for r in range len s:
            # while there are duplicates in current window: (while s[r] is in our set)
                # remove s[l]
                # move l up by 1
            # add s[r] to set
            # compare max_len & update if needed

        # return max_len

    # s       z x y c b a y d e x a z # answer is 7
    #         l
    #                     r
  
    # set: { } # all the unique chars we've seen in current window
    # max_len: 0 # biggest window len we've seen so far

    # window visualization: ''
                

        
        

