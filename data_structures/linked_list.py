from dataclasses import dataclass


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

node1 = Node("data", node2)
node2 = Node()
