#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

"""
  V
[22.0, 5.555555555555555, 1.9787234042553192, 1.7954545454545454, 1.5384615384615385,
    1.4901960784313726, 1.391304347826087, 0.38235294117647056, 0.27692307692307694, 0.015151515151515152]

index | cost | value
=======================
1     |  42  |    81
2     |  42  |    81
3     |  42  |    81


"""


def knapsack_solver(items, capacity):
    bag = []
    values = []
    bag_hash = {}
    total_cost = 0
    total_value = 0

    for item in items:
        bag_hash[item.value/item.size] = [item.index, item.size, item.value]
        values.append(item.value/item.size)

    values = sorted(values, reverse=True)

    for value in values:

        if (total_cost + bag_hash[value][1]) > capacity:
            next
        else:
            total_cost += bag_hash[value][1]
            total_value += bag_hash[value][2]
            bag.append(bag_hash[value][0])

    return {"Value": total_value, "Chosen": sorted(bag)}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
