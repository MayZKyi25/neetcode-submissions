class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        seen = {}
        for i in range(len(nums)):
            res = target - nums[i] 
            if res in seen: 
                return [seen[res], i ] 
            # ask which one is the number {num: index}
            
            seen[nums[i]] = i 
        
    
                

    #     nums = [3, 4, 5, 6, 7]
    #     target = 13
    # # for the current num, what number do I need(compliment_num) to reach the target. 
    # nums:       3 4 5 6 7 
    # compliment:10 9 8 7 6

    # # have we seen that number in our dictionary? 
    # seen in {}? 
    # at num = 3, have we seen a 10 in our dictionary? No --> add it at idx 0 --> seen = {3:0}
    # at num = 4, have we seen a 9 in our dictionary?  No --> add 9 at idx 1 --> seen = {3:0, 4:1, }
    # at num = 5, have we seen a 8 in our dictionary?  No --> add 8 at idx 2 --> seen = {3:0, 4:1, 5:2}
    # at num = 6, have we seen a 7 in our dictionary?  No --> add 7 at idx 3 --> seen = {3,0, 4:1, 5:2, 6: 3}
    # at num = 7, have we seen a 6 in our dictionary?  Yes, it's at index 3, so return seen[nums], nums [i] 

    







        