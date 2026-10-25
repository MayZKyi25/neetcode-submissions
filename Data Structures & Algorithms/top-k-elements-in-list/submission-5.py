class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,8,8,5,5,10,10,10], k = 2, OP: [10,5,8]
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for num, freq in counts.items(): 
            buckets[freq].append(num)
        
        for cur_bucket in reversed(buckets): #bucket
            res.extend(cur_bucket)
            if len(res) >= k :
                return res

    

        

        
        