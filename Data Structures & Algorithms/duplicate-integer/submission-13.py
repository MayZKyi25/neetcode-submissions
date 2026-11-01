class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # init empty set
        # loop throu num
            # if num not in the set
                # return True (no duplicate)
            # add num to the empty set
        # return False 


        distinctNum = set()
        for num in nums: 
            if num in distinctNum:
                return True
            distinctNum.add(num)
        return False




            


        