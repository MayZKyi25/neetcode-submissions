class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # at the current number, what's the number i need to find to get to the target
        # target = 7
        # nums: 3   4   5   6
        #---------------------
        # need: 4   3   2   1

        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_find = target - num 
            if num_to_find in num_to_index:
                return [num_to_index[num_to_find],i]
            num_to_index[num]= i

































        # initialize an empty hashmap called seen
        # loop through each index i in nums:
            # calculate the number needed to reach the target: num_needed = target - nums[i]
            # if num_needed is already in seen:
                # return the index of num_needed and the current index: [seen[num_needed], i]
            # otherwise, store the current number and its index: seen[nums[i]] = i




        # need a dictionary that store {"visted_num": it's idx}
        # trip up part, forgetting we're assigning idx to num
        # return what's seen[req_num] <-- is not element, cuz it's accessing it's value through the key and we store the index


        






        # seen = {}
        # for i, num in enumerate (nums):
        #     num_needed = target - num
        #     if num_needed in seen: 
        #         return [seen[num_needed], i]
        #     seen[num] = i 

            


        
                



    







        