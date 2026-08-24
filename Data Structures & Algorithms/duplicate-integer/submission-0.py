class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for current_num in nums:
            if current_num in my_dict:
                return True
            else:
                my_dict[current_num] = 1
        return False 




    