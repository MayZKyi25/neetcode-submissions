class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len of s and t are differnt, they're not anagram
        # build s, subtract t and if two lens are not 0, they are not anagram
        # need count 
        
        count = [0] * 26 

        if len(s) != len(t):
            return False
        
        for i in range(len(s)): 
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count: 
            if c != 0:
                return False
        return True  
             
      
        