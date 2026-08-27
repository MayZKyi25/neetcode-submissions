class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Best Approach: alphabet indexing: frequency counter
        # Hash Table, key must be immutable! Use tuple or strs (immutable)
        # remember to use ord at current char - ord('a')

        # create a dictionary to store our anagrams 
        # loop each_word throu strs: 
            # initialize encoder for counting our letters [00000000000000000000000]: list type
            # for each char in the word: 
                # encoder = [ord(each char) - ord('a')] 
                # encoder += 1 
            # change to strs/tuple(encoder) so that it's hashable/immutable then append word
        # return the list of (encoder.values())

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


        # Approach 2: sorting approach 
        # need to return a list of anagrams

'''
        { sorted word: [anagram1, anagram2, anagram3]
    
            ____: ["act", "tac", "cat"]
            ____: ["tops, "pots", "stop"]
        }
        '''
        # create a default dict (key: sorted strs, values: anagrams)

        # loop through the strs
            # sorted will return a list of char -> rejoin using "".join(____) to get strs
            # append each anagram to its key

        # return 

        # my_dict = defaultdict(list)
        # for i in range(len(strs)):
        #     sorted_word = "".join(sorted(strs[i]))
        #     my_dict[sorted_word].append(strs[i])
        # return list(my_dict.values())
            

    


                
            

        


        

    





        
        