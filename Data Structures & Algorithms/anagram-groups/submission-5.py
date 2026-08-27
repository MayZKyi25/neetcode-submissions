class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i])) 
            my_dict[sorted_word].append(strs[i])
        return list(my_dict.values())
            

    


                
            

        


        

    





        
        