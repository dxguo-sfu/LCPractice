import sys
import io
from typing import List

class Solution:
    """Docstring to solution class"""
    def __init__(self):
        return

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for index, value in enumerate(nums):
        #     match = target - value
        #     for index2, value2 in enumerate(nums[index+1:]):
        #         # print(F"value: {value}\tvalue2: {value2}")
        #         if value2 == match:
        #             return [index, index + index2 + 1]

        d = dict()

        for index, value in enumerate(nums):
            match = target - value
            if match in d:
                return [d[match], index]
            d[value] = index



def main():
    solution = Solution()

    # Given nums = [2, 7, 11, 15], target = 9,
    # Because nums[0] + nums[1] = 2 + 7 = 9,
    # return [0, 1].

    nums: List[int] = [2, 7, 11, 15]
    target = 26

    pair = solution.twoSum(nums, target)

    print(pair)

if __name__ == '__main__':
    main()
