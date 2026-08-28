class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # sorting is O(nlogn)
        # it wants T: O(n) 
        # the count of the longest sequence
        # <-------1,2,3,4------------------------100------------200--------->
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest