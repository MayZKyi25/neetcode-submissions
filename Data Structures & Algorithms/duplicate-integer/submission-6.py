class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for n in nums:
            if n in myset:
                return true # duplicate found
            myset.add(n)
        return False 




    