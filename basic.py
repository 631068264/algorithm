#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/5 11:42
@annotation = '' 
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return ",".join([str(item) for item in self.items])


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Link:
    def __init__(self):
        self.head = None
        self._size = 0

    def isEmpty(self):
        return self.head == None

    def add_front(self, data):
        temp = Node()
        temp.data = data
        temp.next = self.head
        self.head = temp

        self._size += 1

    def add_tail(self, data):
        temp = Node()
        temp.data = data

        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = temp

        self._size += 1

    def size(self):
        return self._size

    def search(self, item):
        current = self.head
        found = False
        while current is not None:
            if current.data == item:
                found = True
                break
            else:
                current = current.next

        return found

    def delete(self, data):
        if self.isEmpty():
            return
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return
        temp = self.head
        while temp:
            previous = temp
            temp = temp.next
            if temp.data == data:
                previous.next = temp.next
                self._size -= 1
                break

    def print_link(self):
        temp = self.head
        while temp:
            print(temp.data, end=",")
            temp = temp.next
        print()

    def reverse(self):
        if self.head:
            tail = None
            current = self.head
            while current:
                future = current.next
                current.next = tail
                tail = current
                current = future
            self.head = tail
            self.print_link()


# class OrderedLink:
#     def __init__(self):
#         self.head = None
#
#     def search(self, item):
#         current = self.head
#         found = False
#         stop = False
#         while current != None and not found and not stop:
#             if current.data == item:
#                 found = True
#             else:
#                 if current.data > item:
#                     stop = True
#                 else:
#                     current = current.next
#
#         return found
#
#     def add(self, item):
#         current = self.head
#         previous = None
#         stop = False
#         while current != None and not stop:
#             if current.data > item:
#                 stop = True
#             else:
#                 previous = current
#                 current = current.getNext()
#
#         temp = Node()
#         temp.data = item
#         if previous is None:
#             temp.next = self.head
#             self.head = temp
#         else:
#             temp.next = current
#             previous.setNext(temp)
#
#     def isEmpty(self):
#         return self.head == None
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             current = current.getNext()
#
#         return count


if __name__ == '__main__':
    mylist = Link()

    mylist.add_front(31)
    mylist.add_front(77)
    mylist.add_front(17)
    mylist.add_front(93)
    mylist.add_front(26)
    mylist.add_front(54)
    mylist.print_link()

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add_tail(100)
    mylist.print_link()
    print(mylist.search(100))
    print(mylist.size())

    mylist.delete(54)
    mylist.delete(100)
    mylist.print_link()
    print(mylist.size())
