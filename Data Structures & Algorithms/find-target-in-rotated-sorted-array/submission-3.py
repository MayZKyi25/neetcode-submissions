class Solution:
    # 2-pass b-search
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r] or len(nums) == 1:
            return self.search_section(l, r, target, nums)

        pivot = None
        
        # 1st perform b-search to find pivot
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m - 1]:
                pivot = m
                break
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        # figure out if we are gonna perform 2nd b-search on right or left side of pivot
        if nums[0] > target: # target is on the right side
            l, r = pivot, len(nums) - 1 
        else:
            l, r = 0, pivot

        return self.search_section(l, r, target, nums)

    # normal b-search helper
    def search_section(self, l, r, target, nums):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
        