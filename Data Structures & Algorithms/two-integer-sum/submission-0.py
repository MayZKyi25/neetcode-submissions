class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize an empty dict, value: index
        # for i, n in nums: 
            # y = target - nums [i]
            # if y in seen:
                # return [i, dict[y]]
            #if there isn't,

        # [3 4 5 6]
        # seen: {4(y): 0(i)} 
        # index i:
        # n: 
        # y = target - nums [i] = 7 - 3 = 4
        # seen[0] = y

        seen = {} # seen {3:0}
        for i, n in enumerate(nums): 
            y = target - nums[i] # y = 3
            if y in seen: 
                return [seen[y], i] 
            seen[n] = i 

        # if we find the complement in the array, we'll find the answer. 







        