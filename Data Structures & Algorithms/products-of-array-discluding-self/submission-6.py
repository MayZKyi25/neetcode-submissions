class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # num: -1  0  1  2  3 
        # -1 * 1 
        # prod = -1 
        # [1]
        
        l_arr = [1] * (len(nums))
        r_arr = [1] * (len(nums))
        res = [1] * (len(nums))
        prod = 1 

        for i in range(len(nums)):
            l_arr[i] = prod
            prod *= nums[i]
        prod = 1 

        for i in range(len(nums)-1, -1,-1):
            r_arr[i] = prod
            prod *= nums[i]

        for i in range(len(nums)): 
            res[i] = l_arr[i] * r_arr[i]
        return res
        


        # init l_arr, r_arr, res

            # init prod
            # loop thru nums
                # l_arr[i] = prod
                # prod *= nums[i]
            
            # loop thru nums
                # fill in r_arr
            
            # loop thru res
                # fill in res with l_arr[i] * r_arr[i]

            # return res
