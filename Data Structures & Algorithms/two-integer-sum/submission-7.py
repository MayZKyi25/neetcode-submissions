class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} 
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in seen: 
                return [seen[to_find],i]
            seen[num] = i 
            


        