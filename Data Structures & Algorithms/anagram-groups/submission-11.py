class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        for s in strs: 
            count = [0] * 26 
            for i in range(len(s)): # act 
                count[ord(s[i]) - ord('a')] += 1
            anagrams[str(count)].append(s)
        return list(anagrams.values())



