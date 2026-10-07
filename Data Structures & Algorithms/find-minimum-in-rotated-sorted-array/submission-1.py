class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur_min = nums[0]
        l = 0 
        r = len(nums)-1

        while l <= r: 
            if nums[l] < nums[r]:
                cur_min = min(cur_min, nums[l])
                break
                
            m = (l+r)//2 
            cur_min = min(nums[m], cur_min)
            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m-1
        return cur_min
        
        