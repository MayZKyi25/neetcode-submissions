class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1 # 1 # 
        res = [1] * len(nums) # [1 1 1 1]

        for i in range(len(nums)):       #      0 1 2 3
            res[i] = prod    # res [1 1 2 8 ] 
            prod *= nums[i]  # prod 1 2 8 24

        prod = 1
        for i in range(len(nums)-1, -1, -1): # range(3,-1,-1)n 
            res[i] *= prod 
            prod *= nums[i]
        
        return res
            

        

                            