class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # ele is num : [-x- -- -8- -9- -7- -- -- -- -- -- -- ]

        # example nums: [7,7,7,7,8,8,9,9,9]

        # {7:4, 8:2, 9:3} {k: v , where k = actual num, v = freq}
        # bucket = [[], [], [8], [3], [7], [], [], [], [], [], []]
        # freq:      0   1   2    3    4    5   6   7   8   9  10

        
        # init an empty hashmap to count {7:4, 8:2, 9: 3}
        # init the bucket array with size of num of length + 1 
        

        # loop through the nums: 
            # update count[num] with 1, every you see the same key

            # for each key,value in count: 
        
        count = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:           #[7,7,7,7,8,8,9,9,9]
            count[num] += 1        #{7:4, 8:2, 9:3} {k: v , where k = actual num, v = freq}
        
        for num,freq in count.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res
        

       

            

        
        
        
            



        



































        # {
        #     ___: ___
        #     ___: ___
        #     ___: ___
            
        # }
        # key : count 
        # 1   :   1   # number 1 appears 1 time
        # 2   :   2   # number 2 appears 2 time
        # 3   :   3   # number 3 appears 3 time
        # 4   :   2   # number 4 appears 2 time 

        # k = 2 
        # # How do I get the k numbers with the biggest counts?
        # # sort the counts from highest --> lowest using

        # {1: 1, 2: 2, 3: 3}
        # 1, 2, 3 
        # 3, 2, 1

        # num_to_freq_high_to_low = {3: 3, 2: 2, 1: 1} 
        #                             0       1    2 
        # dict [:k ]

       










































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


        


        
        