class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize variable to keep track of current LCP. initialize as strs[0]
        current_LCP = strs[0]  # dance

        # loop thru strs
        for j in strs: 
            # find LCP between current LCP & current str
            current_LCP = self.findLCP(current_LCP, j)
        # return LCP
        return current_LCP


    # new method: find LCP for 2 args
    def findLCP(self, s1: str, s2: str) -> str:
        # loop starting w/ idx 0
        for i in range(min(len(s1), len(s2))):
            # compare s1[i] w/ s2[i]
            if s1[i] != s2[i]:
                # if not equal, return s1[0:i]
                return s1[0:i]
        return s1[0:min(len(s1), len(s2))]


    



