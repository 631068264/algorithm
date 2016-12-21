#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/26 20:23
@annotation = '' 
"""
from collections import OrderedDict
from collections import deque

from heap import ObjectPriorityQueue


class HuffmanNode(object):
    def __init__(self, data, priority):
        self.priority = priority
        self.data = data
        self.left = None
        self.right = None


class HuffmanTree(object):
    def __init__(self, message=None):
        self._message = message
        self._queue = ObjectPriorityQueue(priority_key="priority")
        self._huffman_node = OrderedDict()
        self._root = None
        self._decode_code = {}
        if message is not None:
            self.build_by_message()

    def build_by_message(self, message=None):
        self._message = self._message if self._message else message
        if not self._message:
            raise Exception("The message should be set")
        self._create_priority()
        self._create_tree()
        self._create_huffman_code()

    def build_by_weight(self, weight_dict: OrderedDict):
        """
        Why OrderedDict ?
        Because when weight is the same ,the huffman_code may has different result which may affect the order
        for the ObjectPriorityQueue

        Example:
            OrderedDict([
                (node_name,weight),
                (node_name,weight),
                ...
            ])
        :param weight_dict:
        :return:
        """
        if not weight_dict or not isinstance(weight_dict, OrderedDict):
            raise Exception("The format of weight_dict is {node_name:weight}")
        for node_name, weight in weight_dict.items():
            self._huffman_node[node_name] = {
                "priority": weight,
                "code": "",
            }
        self._create_tree()
        self._create_huffman_code()

    def encode(self, message):
        code = ""
        for m in message:
            code += self._huffman_node[m]["code"]
        return code

    def decode(self, code):
        result = ""
        while code:
            temp = []
            for c in code:
                temp.append(c)
                key = "".join(temp)
                if self._decode_code.get(key):
                    result += self._decode_code[key]
                    code = code[len(temp):]
                    break
        return result

    def _create_priority(self):
        for code in self._message:
            self._huffman_node.setdefault(code,
                                          {
                                              "priority": 0,
                                              "code": "",
                                          })
            self._huffman_node[code]["priority"] += 1

    def _create_tree(self):
        """
            left    right
            0       1
            the smaller one is on the left
        :return:
        """
        for k, v in self._huffman_node.items():
            self._queue.put(HuffmanNode(k, v["priority"]))
        while self._queue.qsize() != 1:
            s1 = self._queue.get()
            s2 = self._queue.get()

            node = HuffmanNode(None, s1.priority + s2.priority)
            node.left = s1
            node.right = s2

            self._queue.put(node)
        self._root = self._queue.get()

    def _create_huffman_code(self):
        current = self._root
        stack = []
        code = []
        while current or stack:
            if current:
                if current.right is None:
                    self._huffman_node[current.data]["code"] = "".join(code)
                    self._decode_code["".join(code)] = current.data
                    # let code and stack are at the same node
                    # because code may at the node which is None
                    code.pop()
                code.append("0")
                stack.append(current)
                current = current.left
            else:
                code.pop()
                current = stack.pop()
                current = current.right
                code.append("1")

    def get_huffman_code(self):
        return self._huffman_node


class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        while current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
            if current is None:
                return None
        print(current.data)
        return current

    def insert(self, data):
        temp = Node()
        temp.data = data
        if self.root is None:
            self.root = temp
        else:
            current = self.root
            while True:
                previous = current
                if data < current.data:
                    current = current.left
                    if current is None:
                        previous.left = temp
                        return
                else:
                    current = current.right
                    if current is None:
                        previous.right = temp
                        return

    def preOrder(self, root):
        if root is not None:
            print(root.data, end=",")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def pre_Order(self, root):
        stack = []
        current = root
        while current is not None or len(stack) != 0:
            if current:
                print(current.data, end=",")
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end=",")
            self.inOrder(root.right)

    def in_Order(self, root):
        stack = []
        current = root
        while current is not None or len(stack) != 0:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data, end=",")
                current = current.right

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=",")

    def post_Order(self, root):
        stack = []
        current = root
        previous = None
        while current is not None or len(stack) != 0:
            while current is not None:
                stack.append(current)
                current = current.left
            if stack[-1].right is not previous:
                current = stack[-1].right
                previous = None
            else:
                previous = stack.pop()
                print(previous.data, end=",")

    def levelOrder(self, root):
        if not root:
            return
        q = deque([root])
        while q:
            current = q.popleft()
            print(current.data, end=",")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


if __name__ == '__main__':
    # tree = Tree()
    # tree.insert(50)
    # tree.insert(25)
    # tree.insert(75)
    # tree.insert(12)
    # tree.insert(37)
    # tree.insert(43)
    # tree.insert(30)
    # tree.insert(33)
    # tree.insert(87)
    # tree.insert(86)
    # tree.insert(97)
    #
    # # tree.levelOrder(tree.root)
    #
    # tree.preOrder(tree.root)
    # print()
    # tree.pre_Order(tree.root)
    #
    # print()
    # tree.inOrder(tree.root)
    # print()
    # tree.in_Order(tree.root)
    #
    # print()
    # tree.postOrder(tree.root)
    # print()
    # tree.post_Order(tree.root)
    # print()
    #
    # tree.search(120)

    # Huffman
    huffman = HuffmanTree()
    weight_dict = OrderedDict([
        ("a", 3),
        ("b", 1),
        ("c", 1),
        ("d", 1),
    ])

    # huffman.huffman_by_message("abacda")
    huffman.build_by_weight(weight_dict)
    print(huffman.encode("abacda"))
    print(huffman.decode("01100111100"))
