#!/usr/bin/python

import argparse

"""
# set the min price default to first index of passed in  elements
# profit: flaot("-inf")

# loop through all the indexs of passed list and check to see if curr index is less that current min buy in if
  # set the min price to the current index if not make no change

"""

# Brute force O(n^2)


def find_max_profit(prices):
    lowest_price = prices[0]
    max_profit = float("-inf")

    for i in range(len(prices)):
        if lowest_price > prices[i]:
            lowest_price = prices[i]
        for j in range(i+1, len(prices)):
            current_profit = prices[j] - prices[i]
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit


# def find_max_profit(prices):
#     max_profit = float("-inf")
#     series = {}

#     for i in range(len(prices)):
#         series[prices[i]] = i

#     prices_sorted = sorted(prices)

#     """

#     0  1    2     3    4
#     2 270 1050  1540  3800

#     i                      -1
#     v                      v
#     2, 270, 1050, 1540, 3800
#     """

#     for i in range(len(prices_sorted)):
#         current_profit = prices_sorted[-1] - prices_sorted[i]
#         if current_profit > max_profit:
#             max_profit = current_profit

#     return max_profit


# find_max_profit([1050, 270, 1540, 3800, 2])
if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


# End Goal: Find the MAX difference / profit between smallest and largest prices

# given a list we need to sort it
# possible sort merge the list
# max profit is found by min_price - (min_price - n)
# the price we subtract by CAN NOT come after it in the list

"""
[2, 270, 1050, 1540, 3800]

min_price = 2


"""
