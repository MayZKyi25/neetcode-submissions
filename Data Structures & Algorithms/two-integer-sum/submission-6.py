class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums:   3   4   5   6
        target: 7
        missing:4   3   2   1
        container that tracks to get 7, at our current num 3, 4 is our num_to_find
        '''

        #initialize {}
        # a for loop to visit nums
            # find needed number by subtracting cur_num from target
            # check the needed num is in our {}
                #if yes, return [value of that key,i]
            # assign that num into our dict
        
        seen = {} # num: indx
        for i, num in enumerate (nums):
            num_to_find = target - num
            if num_to_find in seen: 
                return [seen[num_to_find],i]
            seen[num]= i
        return [] 






        