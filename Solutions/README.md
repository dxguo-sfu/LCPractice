# Solutions Reference

## Two-sums (two_sums.py)
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example: Given nums = [2, 7, 11, 15], target = 9, because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

Tools used: 
* Type hinting
* F-strings (string formatting)
* Dictionary (hashmap)
* For-loop enumeration

## Best Time to Buy and Sell Stock I and II
Problem: Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example: Input: [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Not 7-1 = 6, as selling price needs to be larger than buying price.

Tools used:
* Peak and valley approach