class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        catchdupe = set()
        for n in nums: 
            if n not in catchdupe: 
                catchdupe.add(n)
            else: 
                return True
        return False 
