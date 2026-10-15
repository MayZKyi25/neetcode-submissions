class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init 2 freq arrays
        # count matches

        # if 26, return T

        
        # loop thru s2
            # decr l in freq arr
            # if l is now a match, incr matches
            # elif l was prev a match but no longer, decr matches

            # incr l ptr, incr r ptr

            # incr r in freq arr
            # if r is now a match, incr matches
            # elif r was prev a match but no longer, decr matches
            
            # if matches 26, return T
        # return F


        # s1: abc
        # s2: ecbcaade
            #   l r
        
        # s1_arr: [1,1,1,0,0,0...]
        # s2_arr: [1,1,1,0,0,0....]
        # matches: 26

        if len(s1) > len(s2):
            return False

        def get_alpha_idx(char):
            return ord(char) - ord('a')

        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for i in range(len(s1)):
            s1_arr[get_alpha_idx(s1[i])] += 1
            s2_arr[get_alpha_idx(s2[i])] += 1

        matches = 0
        for i in range(len(s2_arr)):
            if s1_arr[i] == s2_arr[i]:
                matches += 1

        if matches == 26:
            return True

        l, r = 0, len(s1) - 1

        while r < len(s2) - 1:
            lost_char_idx = get_alpha_idx(s2[l])
            s2_arr[lost_char_idx] -= 1
            if s2_arr[lost_char_idx] == s1_arr[lost_char_idx]:
                matches += 1
            elif s2_arr[lost_char_idx] + 1 == s1_arr[lost_char_idx]:
                matches -= 1

            l += 1
            r += 1

            gained_char_idx = get_alpha_idx(s2[r])
            s2_arr[gained_char_idx] += 1

            if s2_arr[gained_char_idx] == s1_arr[gained_char_idx]:
                matches += 1
            elif s2_arr[gained_char_idx] - 1 == s1_arr[gained_char_idx]:
                matches -= 1
            
            if matches == 26:
                return True
        return False