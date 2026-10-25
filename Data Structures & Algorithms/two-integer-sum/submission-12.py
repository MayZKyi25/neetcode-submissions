class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need container for that stores {visted num: its idx}
        # find complement to reach the target target-i = complement
        # if we find complement in {}, return [num1 idx ,num2 idx]
        # otherwise [] 

        seen = {} # {num: idx}
        for idx,num in enumerate(nums): #--> 3 at idx 0
            complement = target-num  # complement = 7 - 3 = 4 , 7-4 = 3
            if complement in seen: # 4 not in seen
                return [seen[complement], idx] 
            seen[num] = idx    # seen[4:0, 3:1]
        return []
            
         
        


        