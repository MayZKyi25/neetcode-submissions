class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0 
        lowest_to_buy_so_far = prices[0] 

        # profit = sell - buy
        for i in range(1, len(prices)): 
            profit = prices[i] - lowest_to_buy_so_far

            if profit > max_profit_so_far: 
                max_profit_so_far = profit

            if prices[i] < lowest_to_buy_so_far: 
                lowest_to_buy_so_far = prices[i]
        
        return max_profit_so_far


# buy at 10, sell at 1 --> profit -9
# buy at 1,  sell at 5 --> profit 4
# buy at 1,  sell at 6 --> profit 5
            























        




    '''

    profit = sell - buy(lowest) 
                   
    to_buy
    to_sell
    return max profit

    buying point has to come before selling point

    '''