class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top_r = 0               
        bottom_r = len(matrix)-1 # 2 , matrix[2] = [14,20,30,40]

        while top_r <= bottom_r:
            mid_r = (top_r + bottom_r) // 2 
            if target > matrix[mid_r][-1]: # ex: if target = 34, 34 > 13
                top_r = mid_r + 1 # 1+1 = 2 
            elif target < matrix[mid_r][0]: # ex if target = 3 , 3 < 10
                bottom_r = mid_r - 1
            else: 
                break         
        if not (top_r <= bottom_r): # this is search boundaries for target, and target not found
            return False

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
                
