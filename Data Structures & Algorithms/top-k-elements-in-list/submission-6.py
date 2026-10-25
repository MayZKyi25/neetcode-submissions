class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        for cur_bucket in reversed(buckets):
            res.extend(cur_bucket)
            if len(res) >= k:
                return res

        