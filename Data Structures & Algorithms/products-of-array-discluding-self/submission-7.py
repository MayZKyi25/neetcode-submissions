class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # num:  1   2   4   6
        # res : 1  1    2   8
    
        res = [1] * (len(nums))
        prod = 1 #  the left

        # this is same as building left arr but just renaming it to res       
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]

        prod = 1 
        for i in range(len(nums)-1, -1,-1):
            #res[i] = prod # this assignment would rease
            res[i] *= prod
            prod *= nums[i]
        return res 

      

        