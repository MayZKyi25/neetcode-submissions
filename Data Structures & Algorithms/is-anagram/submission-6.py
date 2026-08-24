class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False
        my_dict = {} 

        for each_char in s: 
          if each_char not in my_dict:
            my_dict[each_char] = 1
          else: 
            my_dict[each_char] += 1 
          

        for each_t in t: 
          if each_t not in my_dict:
            return False
          else: 
            my_dict[each_t] -= 1
        
        for i in my_dict:
          if my_dict[i] != 0:
            return False 
        return True
        
      
      
      
    