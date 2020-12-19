# ---Breadth-First Search---

from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = list()

    def