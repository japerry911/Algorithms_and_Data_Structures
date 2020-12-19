# ---Breadth-First Search---

from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = list()

    def add_child(self, name: str):
        self.children.append(Node(name))
        return self

    # O(v + 3) Time | O(v) Space
    def breadth_first_search(self, array: List[str]) \
            -> List[str]:
        queue = [self]

        while len(queue) > 0:
            current_element = queue.pop(0)
            array.append(current_element.name)
            for child in current_element.children:
                queue.append(child)

        return array


graph = Node("A")
graph.add_child("B").add_child("C").add_child("D")
graph.children[0].add_child("E").add_child("F")
graph.children[2].add_child("G").add_child("H")
graph.children[0].children[1].add_child("I").add_child("J")
graph.children[2].children[0].add_child("K")
expected = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
actual = graph.breadth_first_search(list())
print(f"EXPECTED:\t{expected}")
print("--------------------------------")
print(f"ACTUAL:\t\t{actual}")
