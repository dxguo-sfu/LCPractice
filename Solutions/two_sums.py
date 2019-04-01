# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    """Docstring to solution class"""
    def __init__(self):
        return

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1
        # for index, value in enumerate(nums):
        #     match = target - value
        #     for index2, value2 in enumerate(nums[index+1:]):
        #         # print(F"value: {value}\tvalue2: {value2}")
        #         if value2 == match:
        #             return [index, index + index2 + 1]

        # Solution 2
        d = dict()
        for index, value in enumerate(nums):
            match = target - value
            if match in d:
                return [d[match], index]
            d[value] = index

def main():
    solution = Solution()
    nums: List[int] = [2, 7, 11, 15]
    target = 26
    pair = solution.twoSum(nums, target)
    print(pair)