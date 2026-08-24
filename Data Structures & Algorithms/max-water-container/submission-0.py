class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1
        max_area = 0 

        while l < r: 
            width = r - l
            length = min(heights[l], heights[r])
            area = width * length
            #print('width:', width, 'heights:', heights, "area:", area)
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                # keep the higher height = move the lower
                l +=1
            else: 
                r -=1 
            # else: 
            #     if heights[l+1] < heights[r-1]:
            #         r -=1
            #     else:
            #         l +=1
        return max_area


        # init l, r at both ends of list
        # init max_area = 0

        # while l < r:
            # width = r - l
            # height = min(heights[l], heights[r])
            # area = w * h
            # max_area = max(max_area, area)

            # if heights[l] < heights[r]
                # move l
            # elif hr > hl
                # move r
            # else (if they're equal)
                # if next l is < next r
                    # move r
                # else
                    # move l

        # return max_area
        