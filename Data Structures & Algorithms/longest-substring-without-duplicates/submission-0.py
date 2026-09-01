class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    # s       z x y c b a y d e x a z # answer is 7
    #         l
    #                     r

        my_set = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            max_len = max(max_len, (r-l)+1)
        return max_len



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
                

        
        

