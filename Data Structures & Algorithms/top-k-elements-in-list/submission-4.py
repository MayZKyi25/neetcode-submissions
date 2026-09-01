class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)                     # num -> frequency
        bucket = [[] for _ in range(len(nums) + 1)]  # index = frequency
        res = []

        # 1. Count how many times each number appears
        for num in nums:
            count[num] += 1

        # 2. Put each number into the bucket for its frequency
        # Example: if 7 appears 4 times -> bucket[4].append(7)
        for num, freq in count.items():
            bucket[freq].append(num)

        # 3. Start from the highest frequency and move backward
        for i in range(len(bucket) - 1, -1, -1):

            # There can be multiple numbers with the same frequency
            for num in bucket[i]:
                res.append(num)

                # Stop once we have the top k numbers
                if len(res) == k:
                    return res 







































        # '''
        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]

        # nums        = original array
        # my_dict     = where we're storing counts
        # my_dict[i]  = count for number i
        # '''

        # # create an empty dict --> digit_to_count = {}
    
        # # for i in nums:
        #     # if i in digit_to_count: 
        #         #update nums[i] = digit_to_count[i].get(0) + 1
        
        # # sort the values of count and return the k most count in a list of nums

        # #Time: O(n log n)
        # # Space: O(n)
                

        my_dict = {} # key: num [1,2,3], value: count of the num freq

        for i in nums:
            if i in my_dict:
                my_dict[i] = my_dict[i]+ 1
            else: 
                my_dict[i] = 1
        # Sort the dictionary keys based on their counts/values, from biggest count to smallest
            sorted_numbers = sorted(my_dict, key = my_dict.get(), reverse=True)

        return sorted_numbers[:k]




        #         [ 1, 1, 1, 8, 8, 9, 10, 10 ] n
#         k = 3
#         {
#             1: 3
#             10: 2
#             8: 2
#             9: 1
#         }
        # key: number itself
        # value: number's frequency


    # create freq counter dict based on nums

    # create buckets list of empty lists, of size len(nums) + 1

    # loop thru each key in freq dict
        # buckets[value].append(key)

    # init res list
    # loop backwards thru buckets
        # if len(res) == k
            # return res
        # if cur bucket is not empty
            # append bucket items to res

        counts = Counter(nums)
        buckets = [ [] for i in range(len(nums) + 1) ]

        for num in counts:
            freq = counts[num]
            buckets[freq].append(num)

        res = []
        for cur_bucket in reversed(buckets):
            if len(res) == k:
                return res
            res.extend(cur_bucket)

    
        

        

# buckets: [_ 9 [10, 2] 1 _ _ _ _ _] (size: n + 1)

# # end desired result:
# [ [],[9],[8, 10], [1], [], [], [], [], [] ]
#   0  1.  2.       3.  4. 5. 6. 7. 8    (idx represents frequency)


        


        
        