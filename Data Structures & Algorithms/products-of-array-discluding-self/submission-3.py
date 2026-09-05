class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, suffix = [], []
        for i in range(len(nums)):
            prefix.append(math.prod(nums[:i]))
            suffix.append(math.prod(nums[i+1:]))
        return [prefix * suffix for prefix, suffix in zip(prefix, suffix)]