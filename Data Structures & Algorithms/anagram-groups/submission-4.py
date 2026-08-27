class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)
        for i in range(len(strs)):
            sorted_char = sorted(strs[i])
            sorted_word = "".join(sorted_char) 
            my_dict[sorted_word].append(strs[i])
        return list(my_dict.values())
            

            # if sorted_word not in my_dict: 
            #     my_dict[sorted_word] = strs[i]
            # print(my_dict.values())


                
            

        


        

    





        
        