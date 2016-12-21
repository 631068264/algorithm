#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/5 12:11
@annotation = '' 
"""
base_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# base = len(base_list)


def encode(num: int, base):
    result = []
    if num == 0:
        result.append(base_list[0])

    while num > 0:
        result.append(base_list[num % base])
        num //= base

    return "".join(reversed(result))


def decode(code: str, base):
    num = 0
    code_list = code
    for index, code in enumerate(reversed(code_list)):
        num += base_list.index(code) * base ** index
    return num


def _encode(num, base):
    if num < base:
        return base_list[num]
    else:
        return _encode(num // base, base) + base_list[num % base]


def _decode(code, *, base):
    if not code:
        return None
    index = len(code) - 1
    if len(code) == 1:
        return base_list.index(code) * base ** index
    return _decode(code[1:], base=base) + base_list.index(code[0]) * base ** index


if __name__ == '__main__':
    print(encode(341413134141, len(base_list)))
    print(decode("60FoItT", len(base_list)))

    print(_encode(341413134141, len(base_list)))
    print(_decode("60FoItT", base=len(base_list)))
