class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs: 
            count = [0] * 26
            for char in range(len(word)):
                count[ord(word[char]) - ord('a')] += 1 
            anagrams[str(count)].append(word)
        return list(anagrams.values())


        
                
