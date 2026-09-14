class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

    
    # optimal sliding window (where we dont recalculate max count when moving L):

        counts = defaultdict(int)
        max_ct = 0 #
        max_len = 0
        l = 0

        for r, c in enumerate(s):
            counts[c] += 1
            max_ct = max(counts[c], max_ct) #
            while (max_ct + k) < (r - l + 1): #
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len
        