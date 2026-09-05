class Solution:
    def containsdup(nums: list[int]) -> bool:
        myset = ()
        for n in nums:
            if n in myset:
                return true # duplicate found
            myset.add(n)
        return False 




    