class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for num in nums: 
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False 

 
                
        # initialize an empty set() 
        # for num in nums: 
            # if num in the set:
                # return False
            # else (num not in the set, unique)
                # add num into the set 
                # return True
        