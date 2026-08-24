class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: sorted_wrod
        # value: orginal list of words = word
        
        groups = {} 
        for word in strs: 
            sorted_word = ''.join(sorted(word))
            if sorted_word not in groups: 
                groups[sorted_word] = []
            groups[sorted_word].append(word)
        return list(groups.values())




        '''
        
        Input: strs = ["act","pots","tops","cat","stop","hat"]

        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        sort strs act cat"

        - sorted all strs 
        - for each element in sorted 
        - {cat: 1} 
        - return the unsorted strs 
        
        '''
        # create an empty dictionary
        # sort each word in the strs
        # check if each sorted word in the dict
        
        # groups = {"act": ["act", "cat"], ["hat": "hat"] }

    


            



        
        
            
            

            

        

    

        

    





        
        