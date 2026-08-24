class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0 
        r = len(numbers) - 1

        while l < r: 
            if numbers[l] + numbers [r] == target:
                return [l+1, r+1]
            if numbers[l] + numbers [r] > target: 
                r -= 1 
            if numbers[l] + numbers [r] < target: 
                l += 1
        return [l+1, r+1]































        # # idx        1 2 3 4 5 6 7
        # # numbers = [1,2,4,5,6,7,8], target = 9 
        # # wanted to start at index 1 
        # # ans: [3,4]

        # # left = 1
        # # right = len(numbers)

        # # 9 - numbers[l] = numbers [r]

        # l = 0
        # r = len(numbers) - 1
        
        # while l < r: 
        #     mid = (l + r)// 2  # 4 nums[4] = 5 
        #     # we get 5 from mid, we want to find 4 
        #     ans = target - numbers[mid]   # 3 - 2 = 1
        #     numbers[l] + numbers [r] == target

        #     if ans < numbers[mid]: #1 < 2 
        #         r = mid -1 
        #     else:
        #         l = mid + 1 
        # return [l+1,r+1]

            


        