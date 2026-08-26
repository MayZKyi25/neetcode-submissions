class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums: -4  -1  -1    0   1   2 

        res = []
        nums = sorted(nums)

        for i in range(len(nums)-2): # you still need 2 numbers after it for l and r.
            l = i + 1
            r = len(nums) - 1


            if i > 0 and nums[i] == nums [i-1]:
                continue
            
            while l < r:
                total = nums[i] + nums [l] + nums[r]

                if total == 0: 
                    res.append([nums[i],nums[l],nums[r]])
                    #nums: -4  -1  -1  -1  0   1  2  2   2 (and found [-1, -1, 2] as triplet)
                    #       fix i          l    r

                    l += 1  # move the pointer after triplet is found
                    r -= 1  # move the pointer after triplet is found

                    while l < r and nums[l] == nums [l-1]:
                        l += 1  # move the pointer due to prev duplicate element
                    
                    while l < r and nums[r] == nums [r+1]: 
                        r -= 1  # move the pointer due to prev duplicate element

                
                elif total > 0:
                    r -= 1
                
                else: 
                    l += 1
        
        return res
            






            



        
        
            

                

            



