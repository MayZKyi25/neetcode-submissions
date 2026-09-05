class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):        # i=0
            x=1
            for j in range(len(nums)):     # j=0     | j=1     | j=2     | j=3
                if i!=j:
                    x*=nums[j]      #Skip    |x=1*2=2  | x=2*4=8 | x=8*6=48
            output.append(x)
        return output


        # product = [1] * len(nums) 
        # <----1------- i= 2 ------4 ------6 -----> 
        # # prefix []
        # # sufix [] 
        # # iterate through num: 
        # # nums = [1,2,4,6]

        # for i in range (1, len(nums)):

