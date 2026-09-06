class Solution:
    def trap(self, height: List[int]) -> int:        

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        current_max_l = 0 
        current_max_r = 0 
        trapped_water = 0 
    
        for l in range(1,len(height)):
            current_max_l = max(current_max_l, height[l-1])
            left_max[l] = current_max_l

        for r in range(len(height) - 2, -1, -1):
            current_max_r = max(current_max_r, height[r + 1])
            right_max[r] = current_max_r
        
        for w in range(len(height)):
            possible_water = min(left_max[w], right_max[w]) - height[w]

            if possible_water > 0:
                trapped_water += possible_water
        return trapped_water
       
        # index:      0  1  2  3  4
        # height:     1  3  3  2  4
        # left_max:   0  1  3  3  3
        # right_max:  4  4  4  4  0        
        
        # 1. Create:
        #    left_max  = array of 0s
        #    right_max = array of 0s
        #    water = 0

        # 2. Find tallest wall to the LEFT of each index:
        #    - start at index 1
        #    - look at height[i - 1]
        #    - update current_max_left
        #    - store current_max_left in left_max[i]

        # 3. Find tallest wall to the RIGHT of each index:
        #    - start at second-to-last index
        #    - move backwards
        #    - look at height[i + 1]
        #    - update current_max_right
        #    - store current_max_right in right_max[i]

        # 4. For every index i:
        #    possible_water = min(left_max[i], right_max[i]) - height[i]

        #    if possible_water > 0:
        #        add it to water

        # 5. return water






























    





        

        
        