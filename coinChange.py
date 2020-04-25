class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # [1, 2, 5]
        # 11
        
        # [0, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf]
        
        # 1
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        
        # 1
        # 2
        
        #  0  1  2  3  4  5  6  7  8  9  10 11
        
        # [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
        
        # 1
        # 2
        # 5
        
        #               1 step for 5
        #                  ----------------
         #                 |              |
        #  0  1  2  3  4  5  6  7  8  9  10 11
        
        # [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        
        
        # array with steps
        # loop through coins
            # loop from coin to amount
                # numOfStemps1 = steps[i]
                # numOfSteps2 = steps[i - coin] + 1
                # steps[i] = min(numOf)
                
        steps = [0] + [float('inf')] * amount
        # [0, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf, Inf]
        
        for coin in coins:
            for i in range(coin, amount + 1):
                stepsAtIdx = steps[i]
                stepsAtPrevIdx = steps[i - coin]
                steps[i] = min(stepsAtIdx, stepsAtPrevIdx + 1)
        
        if steps[-1] == float('inf'):
            return -1
        
        return steps[-1]
            
            