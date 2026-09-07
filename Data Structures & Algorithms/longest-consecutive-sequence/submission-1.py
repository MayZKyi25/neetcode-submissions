class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        
        sorted_n = sorted(set(nums))
        longest = 1 
        cur_longest = 1 
        #[2, 3, 4, 4, 5, 10, 20]
        

        for i in range(1, len(sorted_n)): 
            if  sorted_n[i] == sorted_n[i-1] + 1:
                cur_longest += 1
            else:
                cur_longest = 1
            longest = max(longest, cur_longest)
        return longest
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         if not nums:
#             return 0

#         sorted_nums = sorted(set(nums))
#         longest = 1
#         current_longest = 1

#         for i in range(1, len(sorted_nums)):
#             if sorted_nums[i] == sorted_nums[i - 1] + 1:
#                 current_longest += 1
#             else:
#                 current_longest = 1
#             longest = max(longest, current_longest)

#         return longest

       




        
        
