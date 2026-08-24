class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        nums = [-4, -1, -1, 0, 1, 2]

        idx :   0   1   2   3   4   5
        -----------------------------
        nums:  -4  -1  -1   0   1   2
        -----------------------------
                        i   l        r
        
        When idx = 0, nums = -4, -4-1+2 = -3 < 0  (increase our left pointer when sum < 0 )
        since we already visited -1, when -4+ 1 + 2 = -1 

        i = 1, nums[1] = -1 -1+2 = [-1,-1,2]. append the pair 
        i = 3, nums[2] = -1

        '''
        triplet = [] 
        nums = sorted(nums)

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r] 
                if total == 0: 
                    triplet.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0: 
                    l += 1
                else: 
                    r -= 1
        return triplet 
                
                
           
        # triplet = []
        # sort the numbers 
        # for i in range(len(nums)), 
            # a two pointer, left, right
            # l = i +1, r = len (nums) - 1
                # while l < r: 
                    # check if total sum (-4-1+2) == 0? 
                        # if total == 0: 
                            # found the triplet, append the those into our triplet list

                        # elif total > 0: 
                            # r = r -1

                        # else (total < 0): 
                            # l = l + 1



        # return a list of triplets []

        



