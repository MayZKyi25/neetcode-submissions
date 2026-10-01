class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  target = 3
        #  1   3   5   7
        # 10  11  16  20
        # 23  30  34  60

        r = len(matrix)        # row of the matrix
        #c = len(matrix[0])     # colum of matrix 

        top_r = 0               # first top row
        bottom_r = r - 1        # bottom row 

        while top_r <= bottom_r:
            mid_r = (top_r + bottom_r) // 2 
            if target > matrix[mid_r][-1]: # ex: if target = 34, 34 > 20 
                top_r = mid_r + 1 
            elif target < matrix[mid_r][0]: # ex if target = 3 , 3 < 10
                bottom_r = mid_r - 1
            else: # matrix[mid_r][0] <= target <= matrix[mid_r][-1]
                break         
        if not (top_r <= bottom_r): # this is search boundaries for target, and target not found
        # same as top_r > bottom_r 
            return False

        #matrix[mid_r] is where the target is , mid_r = 0 , matrix[mid_r] = 1 3 5 7  
                                                                            #l   t  h
        #print(matrix[mid_r])

        target_row = matrix[mid_r]

        l = 0 
        h = len (target_row) - 1
        while l <= h: 
            m = (l+ h)// 2
            if target_row[m] == target: 
                return True 
            elif target_row[m] > target : 
                h = m - 1
            else: 
                l = m + 1
        return False 
                

    