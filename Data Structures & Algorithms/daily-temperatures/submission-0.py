class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # temp             : 30    38   30   36   35   40   28
        # mystack: [[30, 0], [38, 1], [30, 2], [36, 3], [35, 4], [40, 5], [28, 6]]

        # [30, 0], [38, 1] 
       
        # Stack stores [temperature, index] for days
        # that are still waiting for a warmer day.
        mystack = []

        # Default is 0 because some days never find a warmer day.
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # Today is warmer than the day at the top of the stack.
            while mystack and temperatures[i] > mystack[-1][0]:
                previous_temp, previous_index = mystack.pop()

                # Calculate how many days the previous day waited.
                res[previous_index] = i - previous_index

            # The current day now waits for a future warmer day.
            mystack.append([temperatures[i], i])

        return res
                    
            


        

        
    

            
     


        


        
        