class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums:   1   2   4   6
        # prod:   1   1   2   8
        res = [1] * len(nums)
        prod = 1 
        for i in range(len(nums)): 
            res[i] = prod
            prod = prod * nums[i]
        prod = 1 
        for i in range(len(nums)-1, -1,-1):
            res[i] = prod * res[i]
            prod = prod * nums[i]
        return res



        
        