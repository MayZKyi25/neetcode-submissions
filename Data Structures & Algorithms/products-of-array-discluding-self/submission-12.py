class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prod = 1 # holds the product of prev index or left values
        res = [1] * len(nums)

        for i in range(len(nums)): 
            res[i] = prod   # assgin the calculated prod into res[i] to store all the left res 
            prod *= nums[i] # this part calculates all left prod before index i 
        
        prod = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i] 
        
        return res



        # nums:   1   2   4   6 
        #                 i  
        # left: 

        
        # res[i] = prod  = 8 
        # prod = nums[i] * prod , i = 4, 2 * 1 = 8
        # # calculate for indx 1 using index 0 value since we wanna know the left value of that 
        # res1:    1   1   2   8
        # nums:    1   2   4   6  
        #          i 
        # resf:    48   24  12   8

        # res[i] *= prod = 8 * 1 


        # right * res[i] = res


        
    
        

        

        