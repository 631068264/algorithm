#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/12 18:15
@annotation = '' 
"""
import math
import random
from operator import attrgetter

from basic import Queue, Stack

"""
无向图、混合图、有向图
相对而言，有向图的通用性更强，因为无向图和混合图都可转化为有向图

无向图，与顶点v关联的边数，称作v的度数(degree)
有向图 分成入度 出度

不含任何自环的图称作简单图simple graph

起止顶点相同 环路
沿途顶点互异 简单通路

"""


class Vertex:
    def __init__(self, name):
        self.name = name
        self.in_degree = 0
        self.out_degree = 0
        self.degree = 0  # For undigraph
        # self.visited = False


class Edge:
    def __init__(self, src, dest, weight, direct):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.direct = direct

    def __repr__(self):
        return "dest:%s,weiht:%s,direct:%s" % (self.dest, self.weight, self.direct)


class Graph:
    def __init__(self, adjacency_list=None, direct=None):
        self.adjacency_list = {} if adjacency_list is None else adjacency_list
        self.direct = direct
        self.vertlist = {}
        # self.visited = set()

    def addEdge(self, src, dest, weight=None, direct=True):
        direct = direct if self.direct is None else self.direct
        # digraph
        link = self.adjacency_list.setdefault(src, [])
        link.append(Edge(
            src,
            dest,
            weight=weight,
            direct=direct)
        )
        link = self.adjacency_list.setdefault(dest, [])
        self._degree(src, dest, direct)
        # undigraph
        if not direct:
            link.append(Edge(
                dest,
                src,
                weight=weight,
                direct=direct)
            )

    def _degree(self, src, dest, direct):
        src_vertx = self.vertlist.setdefault(src, Vertex(src))
        if direct:
            src_vertx.out_degree += 1
        else:
            src_vertx.degree += 1
        self.vertlist[src] = src_vertx

        dest_vertx = self.vertlist.setdefault(dest, Vertex(dest))
        if direct:
            dest_vertx.in_degree += 1
        else:
            dest_vertx.degree += 1
        self.vertlist[dest] = dest_vertx

    def __iter__(self):
        return iter(self.adjacency_list.items())

    def __getitem__(self, item):
        return self.adjacency_list[item]

    def bfs(self, vertex_name):
        visited = set()
        queue = Queue()
        visited.add(vertex_name)
        print(vertex_name, end=",")
        queue.put(vertex_name)
        while not queue.isEmpty():
            vertex = queue.get()
            for edge in self.adjacency_list[vertex]:
                if edge.dest not in visited:
                    visited.add(edge.dest)
                    print(edge.dest, end=",")
                    queue.put(edge.dest)

        print()

    def dfs(self, vertex_name, visited=None):
        visited = set() if visited is None else visited
        visited.add(vertex_name)
        print(vertex_name)
        for edge in self.adjacency_list[vertex_name]:
            if edge.dest not in visited:
                self.dfs(edge.dest, visited)

    def topological_sort(self):
        in_degree = dict((v.name, v.in_degree) for v in self.vertlist.values())
        in_degree0 = [v.name for v in self.vertlist.values() if v.in_degree == 0]
        stack = Stack()
        while in_degree0:
            vertex = in_degree0.pop()
            stack.push(vertex)
            for edge in self.adjacency_list[vertex]:
                in_degree[edge.dest] -= 1
                if in_degree[edge.dest] == 0:
                    in_degree0.append(edge.dest)

        if not len(stack) == len(self.vertlist):
            return False, "There is a circle in the graph"

        print(stack)
        return True, stack

    # relate the num of vertex
    def prim(self, vertex_name=None):
        vertex_name = random.choice(list(self.vertlist.keys())) if vertex_name is None else vertex_name
        visited = set()
        visited.add(vertex_name)
        total_cost = 0
        path = []
        while len(visited) != len(self.vertlist):
            edges = []
            for v in visited:
                for edge in self.adjacency_list[v]:
                    if edge.dest not in visited:
                        edges.append(edge)
            for edge in (sorted(edges, key=attrgetter("weight"))):
                total_cost += edge.weight
                visited.add(edge.dest)
                path.append((edge.src, edge.dest))
                break
        print(path, total_cost)
        return path, total_cost

    def dijkstra(self, vertex_src=None, vertex_dest=None):
        # prepare a distance_graph to get the distance from vertex to vertex
        distance_graph = {}
        for vertex_name, edge_list in self.adjacency_list.items():
            distance_graph[vertex_name] = {}
            for edge in edge_list:
                distance_graph[edge.src][edge.dest] = edge.weight
        for src in self.vertlist.keys():
            for dest in self.vertlist.keys():
                if dest == src:
                    distance_graph[src].setdefault(dest, math.inf)
                else:
                    distance_graph[src].setdefault(dest, math.inf)

        visited = set()
        visited.add(vertex_src)

        nodes = list(self.vertlist.keys())
        nodes.remove(vertex_src)

        path = {vertex_src: {vertex_src: [vertex_src]}}
        d = s = vertex_src
        distance_dict = {vertex_src: 0}

        while nodes:
            min_distance = math.inf
            for src in visited:
                for dest in nodes:
                    # distance = distance_graph[vertex_src][src] + distance_graph[src][dest]
                    distance = distance_dict[src] + distance_graph[src][dest]
                    if distance <= min_distance:
                        min_distance = distance
                        distance_dict[dest] = distance
                        # distance_graph[vertex_src][dest] = distance
                        s = src
                        d = dest
            path[vertex_src][d] = [i for i in path[vertex_src][s]]
            path[vertex_src][d].append(d)
            # distance_dict[d] = min_distance

            visited.add(d)
            nodes.remove(d)
        for vertex_dest, distance in distance_dict.items():
            distance_dict[vertex_dest] = {
                "path": [] if distance == math.inf else path[vertex_src][vertex_dest],
                "distance": distance,
            }

        print(distance_dict)
        return distance_dict


"""
0
1  2  3
46 5
"""
# Traverse
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(1, 6)

# Top sort
# g = Graph()
# g.addEdge(1, 4, 2)
# g.addEdge(2, 4, 4)
# g.addEdge(3, 4, 6)
# g.addEdge(4, 5, 9)
# g.addEdge(4, 7, 1)
# g.addEdge(5, 9, 4)
# g.addEdge(6, 7, 7)
# g.addEdge(7, 8, 8)
# g.addEdge(8, 9, 1)

# MST(minimal spanning tree)
# g = Graph(direct=False)
# g.addEdge(1, 2, 3)
# g.addEdge(1, 4, 2)
# g.addEdge(1, 6, 0)
# g.addEdge(2, 3, 4)
# g.addEdge(2, 4, 4)
# g.addEdge(3, 4, 2)
# g.addEdge(4, 5, 9)
# g.addEdge(4, 7, 1)
# g.addEdge(5, 9, 4)
# g.addEdge(6, 7, 7)
# g.addEdge(7, 8, 8)
# g.addEdge(8, 9, 1)

# short path
g = Graph()
g.addEdge(1, 4, 2)
g.addEdge(2, 4, 4)
g.addEdge(3, 4, 6)
g.addEdge(4, 5, 9)
g.addEdge(4, 7, 1)
g.addEdge(5, 9, 4)
g.addEdge(6, 7, 7)
g.addEdge(7, 8, 3)
g.addEdge(8, 9, 1)
g.addEdge(8, 5, 3)
for k, v in g:
    print(k, v)

# g.dfs(0)
# g.bfs(0)
# g.topological_sort()
# g.prim()
g.dijkstra(4)
# print(float("inf") > 10 ** 10)
# print(sys.float_info)
