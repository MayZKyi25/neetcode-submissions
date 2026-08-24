class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
                 0  1 2 3 4 5 6 7
        prices: [10,1,5,6,7,1,0,2]
        max_profit_so_far: 6
        i: 7       
        prices[i]: 2  
        lowest_buying_price_so_far: 0
        cur_profit: 

        '''
        # init max_profit_so_far
        max_profit_so_far = 0 
        # init lowest_buying_price_so_far
        lowest_buying_price_so_far = prices[0]

        # loop thru prices (starting at idx 1): this represents our cur selling price
        for i in range(1,len(prices)):
            cur_profit = prices[i] - lowest_buying_price_so_far  #1 - 10 = -9 , max-profit_so_far = 0

            # if cur profit (cur selling price - lowest_buying_price) > max_profit
            if cur_profit > max_profit_so_far: 

                # update max_profit
                max_profit_so_far = cur_profit

            # if cur selling price < lowest_buying_price_so_far 
            # [10,1,5,6,7,1,0,2]
            if prices[i] < lowest_buying_price_so_far:    
                # update lowest_buying_price_so_far
                lowest_buying_price_so_far = prices[i]

        # return max_profit_so_far
        return max_profit_so_far
        




    '''
                buy at 1, sell at 7
                -9-5-4-3-9
    prices = [10,1,5,6,7,1]
               0 1 2 3 4 5
    profit = sell - buy(lowest) 
                   
    to_buy
    to_sell
    return max profit

    buying point has to come before selling point

    '''