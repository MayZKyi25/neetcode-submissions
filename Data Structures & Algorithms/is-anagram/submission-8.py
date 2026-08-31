class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
        
        encode_list = [0] * 26
        for char in range(len(s)): # char: index, s: string 
            encode_list[ord(s[char])- ord('a')] += 1 
            encode_list[ord(t[char])- ord('a')] -= 1 # (after this line, if it's anagram, the encode list will be 0)
        
        for val in encode_list: 
            if val != 0: 
                return False
        return True 




        '''
        s = "racecar", t = "carrace"
        if the len of s and t are different, they're out

        alphabetical indexing (postion)

        [0] * 26 that represents a --> z 
        encode_list --> [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0........0]
        idx-->              0 1 2 3 4 5 6 7.................................26
        letter -->          a b c d e f g h .................................z

        # for loop through each character in s: 
            # find out the position of the current_char in s
            # ecode_counter[ord[current_char] - ord('a') ] += 1 
        
        # for loop through each character in t: 
            # encode it and when we see each character we decrease by 1 

        for each_val in encode_list: 
            if encode_list(each_val) != 0: 
                return False
        otherwise, return True 



        
        '''

        print(sorted(s)) 
        print (sorted(t))






























    '''
    # Brute Force: O (nlogn + m log m), n/m = how long str of s/t is
        if len(s) != len(t): 
            return False
        return sorted(s) == sorted(t) 
    '''































      