class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        seen = {}
        for idx in range(len(nums)):
            req_num = target - nums[idx] 
            if req_num in seen: 
                return [seen[req_num], idx ] 
            seen[nums[idx]] = idx 
        
                



    







        