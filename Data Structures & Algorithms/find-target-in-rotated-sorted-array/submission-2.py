class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [4 5 6 7 0 1 2]
        # idx     0 1 2 3 4 5 6
        #                 l m r
        # 1. Which half is sorted?
        # 2. Is target inside that sorted half?
        # 3. If yes, search there.
        # 4. If no, search the other half.
        
        l = 0                            
        r = len(nums)-1                  
        while l <= r:                    
            m = (l+r) // 2               
            if nums[m] == target:       
                return m     

            if nums[l] <= nums[m]:  # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:  # right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1