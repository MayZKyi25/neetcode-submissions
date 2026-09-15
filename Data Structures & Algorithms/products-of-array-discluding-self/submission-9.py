class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # num:  1   2   4   6 
        # prod = 1      # store previous prod and update to res [] 
        # calculating next prod = nums[i] * previous prod = nums[0] * 1 = 1*1 = 1

        prod = 1
        res = [1] * len(nums) # store left, then multiply directly with right prod

        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        
        #resetting the prod as prod now store prod of everything before nums[-1]
        prod = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= prod
            prod *= nums[i] 
        return res
            
        # 1 2 4 6

        # 1    1   2   8
        # 48  24   6   1
        # what's the right arr and * left 

         
         
    

      

        