#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/5 10:03
@annotation = '' 
"""
# print(5 // 2)
#
# l = []
# l.append(3)
# l.insert(4, 4)
# print(l)
#
# myList = [1024, 3, 3, 6.5]
# myList.append(False)
# print(myList)
# myList.insert(2, 4.5)
# print(myList)
# print(myList.count(3))

# l = "David"
# for s in l:
#     print(s)
# f = "D"
# print(f in l)
# print(ord("a"))

# from collections import defaultdict
#
# # 一个key 对应多值multidict
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)
#
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(4)
# print(d)

# dict 最值
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# zip()
# 函数创建的是一个只能访问一次的迭代器。
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print(min_price, max_price)

min(prices, key=lambda k: prices[k])  # Returns 'FB'
max(prices, key=lambda k: prices[k])  # Returns 'AAPL'

print(sorted(prices.items(), key=lambda t: t[0]))
print(sorted(prices.items(), key=lambda t: t[1]))


# dict去重
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: (d['x'], d['y'])))
list(dedupe(a, key=lambda d: d['x']))

# 排序
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter

print(sorted(rows, key=itemgetter('fname')))
print(sorted(rows, key=itemgetter('uid')))

# 对象排序
# print(sorted(rows, key=attrgetter('uid')))

# 分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


def add(x: int, y: int) -> int:
    return x + y


print(add(9, 8))
