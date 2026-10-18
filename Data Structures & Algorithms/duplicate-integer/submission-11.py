class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # key intuation - create a set to hold unique number
        seen = set() 
        for n in nums: 
            if n in seen: 
                return True # duplicate busted
            seen.add(n)
        return False # after adding everything, no duplicate found
    

       
        