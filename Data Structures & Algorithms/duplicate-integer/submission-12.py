class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNum= set() 
        for num in nums: 
            if num in uniqueNum:
                return True
            uniqueNum.add(num)
        return False
            


        