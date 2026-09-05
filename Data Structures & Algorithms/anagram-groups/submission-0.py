class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create an empty dictionary
        # for each word in strs:
            # sort the letters of the current word
            # use the sorted word as the key
            # check if this sorted word already exists in dictionary
                # if yes:
                    # add the ORIGINAL word to that key's list

                # if no:
                    # create a new key
                    # and store the ORIGINAL word in a list

        # return all the lists from the dictionary

        my_dict = {}

        for each_word in strs:
            sorted_word = "".joinsorted(each_word)

            # if sorted word is not already a key
            if sorted_word not in my_dict:
                my_dict[sorted_word] = []

            # add original word to that group
            my_dict[sorted_word].append(word)

        # return all grouped anagrams
        return list(my_dict.values())
        


        

    





        
        