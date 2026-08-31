class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    # Brute Force: O (nlogn + m log m), where n is the len of str s and m is the len of str t
        if len(s) != len(t): 
            return False

        return sorted(s) == sorted (t)


        

        































      