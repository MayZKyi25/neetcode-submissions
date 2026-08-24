class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        '''
        Input: nums = [1,2,2,3,3,3], k = 2

        Output: [2,3]

        nums        = original array
        my_dict     = where we're storing counts
        my_dict[i]  = count for number i
        '''

        # create an empty dict --> digit_to_count = {}
    
        # for i in nums:
            # if i in digit_to_count: 
                #update nums[i] = digit_to_count[i].get(0) + 1
        
        # sort the values of count and return the k most count in a list of nums


        

        my_dict = {} # key: num [1,2,3], value: count of the num freq

        for i in nums:
            if i in my_dict:
                my_dict[i] = my_dict[i]+ 1
            else: 
                my_dict[i] = 1
        sorted_numbers = sorted(my_dict, key=my_dict.get, reverse=True)

        return sorted_numbers[:k]


        # create anagrams defaultdict
        # loop thru strs 
            # create buckets list of size 26 w/ 0 each
            # loop thru word
                # increment bucket based on alpha idx
            # append word into anagrams at key of buckets

        # return list of anagrams values

        anagrams = defaultdict(list)

        for word in strs:
            buckets = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                buckets[idx] += 1
            anagrams[str(buckets)].append(word)

        return list(anagrams.values())

        


        
        