class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for n in nums:
            if n in myset:
                return True # duplicate found
            myset.add(n)
        return False 




    