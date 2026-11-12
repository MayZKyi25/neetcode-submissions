class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # 1. naive solution, uses extra space
        # 2. better solution w/o extra space, but modifies input array
        # 3. solution w/o extra space & doesnt modify array
        
        # nums: [2 6 1 5 1 4 3]
        # idx:   0 1 2 3 4 5 6

        # nums_vistied:[0 0 0 0 0 0 0]
          # idx:        0 1 2 3 4 5 6


        i = 0

        while True:
            if nums[i] == 0: #  nums[1] == 0 
                return i     # return 1 
            temp = nums[i]   # temp = 2 | 1 | 6 | 3 | 5 | 4 | 1 
            nums[i] = 0      # nums[0] = 0 | 0 | 0 | 0 | 0 | 0 | 0
            i = temp         # i = 2 | 1 | 6 | 3 | 5 | 4 | 1

            # cur node is nums[i]
            # if we've already seen this node
                # return i
            # save val of cur node
            # modify val of cur node to 0
            # set i to saved val


               

