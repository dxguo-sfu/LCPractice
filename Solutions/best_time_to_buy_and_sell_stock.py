class Solution:
    """Docstring to solution class"""
    def __init__(self):
        return

    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen_price = sys.maxsize
        max_profit = 0
        for i, v in enumerate(prices):
            if v < lowest_seen_price:
                lowest_seen_price = v
            elif v - lowest_seen_price > max_profit:
                max_profit = v - lowest_seen_price
        return max_profit


def main():
    arr = [7,21,5,3,6,4,10]
    solution = Solution()
    ans = solution.maxProfit(arr)
    print(ans)