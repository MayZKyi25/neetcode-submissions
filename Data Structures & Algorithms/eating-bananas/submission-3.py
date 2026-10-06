class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checkIfWithinH(rate):
            time = 0 
            for pile in piles: 
                time += math.ceil(pile/rate)
                if time > h: 
                    return False
            return True 

        l = 1
        r = max(piles)
        
        res = max(piles) 
        # l--------m---------r
        while l <= r: 
            m = (l+r)// 2 
            if checkIfWithinH(m):
                res = min(m,res)
                r = m-1
            else: 
                l = m+1
        return res 



        


            # time = 0
            # for each pile
                # calculate how many hours it takes to eat that pile: math.ceil(pile / rate)
                # add the # of hours to time
                # if time > h
                    # return False

            # return True

        # perform b search & check each mid with checkIfWithinH until we find lowest rate that works

        # res = max(piles)
        # while l <= r:
            # m = ...
            # if checkIfWithinH(piles[m]) is true
                # update res
                # move left
            # else
                # move right

        # return res