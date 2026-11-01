class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        count = Counter(nums)
        # Counter({1:1, 2: 2, 8: 2, 5: 3 }) num --> req 
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items(): 
            buckets[freq].append(num)
        
        for cur_bucket in reversed(buckets):
            res.extend(cur_bucket)
            if len(res) >= k:
                return res[:k]
        
            
        
    
        