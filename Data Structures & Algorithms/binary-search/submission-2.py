class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if there is only one number in the array return that array 
        l = 0 
        h = len(nums)-1

        while l <= h: 
            mid = (l+h)//2

            if nums[mid] == target: 
                return mid
            
            elif nums[mid] > target: # meaning 5 > 4 
                h -= 1 
            else: 
                l += 1
        
        return -1
    

        