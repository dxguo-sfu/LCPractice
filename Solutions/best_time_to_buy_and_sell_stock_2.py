class Solution:
    """Docstring to solution class"""
    def __init__(self):
        return

    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1
        # total_profit = 0
        # bought = False
        # bought_price = 0
        # num_days = len(prices)

        # for day, v in enumerate(prices):
        #     if day < num_days - 1:
        #         if not bought and prices[day + 1] > v:
        #             bought = True
        #             bought_price = v
        #         elif bought and prices[day + 1] < v:
        #             bought = False
        #             current_profit = v - bought_price
        #             total_profit += current_profit
        #     elif day == num_days - 1 and bought:
        #         current_profit = v - bought_price
        #         total_profit += current_profit

        # return total_profit

        # Solution 2
        total_profit = 0
        days = len(prices)

        for i in range(days - 1):
            total_profit += prices[i+1] - prices[i] if prices[i+1] > prices[i] else 0

        return total_profit



def main():
    arr = [7,21,5,3,6,4,10]
    solution = Solution()
    ans = solution.maxProfit(arr)
    print(ans)