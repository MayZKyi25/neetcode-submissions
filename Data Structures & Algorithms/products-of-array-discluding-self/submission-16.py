class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1 2 4 6] 
        # left prod =  [ 1  1  2 8]
        # right prod = [ 48 24 6 1]
        prod = 1 
        res = [1] * len(nums) # [1 1 1 1]

        for i in range(len(nums)):       
            res[i] = prod    
            prod *= nums[i]  

        prod = 1 # 1, 6, 24, 48 
        for i in reversed(range(len(nums))):
            res[i] *= prod  
            prod *= nums[i] 
        return res
            

        

                            