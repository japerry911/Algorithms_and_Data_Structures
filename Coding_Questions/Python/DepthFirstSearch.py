# ---Depth-First Search---

from typing import List


class Node:
    def __init__(self, name: str):
        self.children = list()
        self.name = name

    def add_child(self, name: str):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array: List[str]) -> List[str]:
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    # def depth_first_search(self, array: List[str], is_root: bool = True) \
    #         -> List[str]:
    #     if is_root is True:
    #         array.append(self.name)
    #
    #     if self.children is not None:
    #         for child in self.children:
    #             array.append(child.name)
    #             child.depth_first_search(array, False)
    #
    #     return array

    # def depth_first_search(self, array: List[str], is_root: bool = True) \
    #         -> List[str]:
    #     current_node = self
    #
    #     if is_root is True:
    #         array.append(current_node.name)
    #
    #     if current_node.children is not None:
    #         for child in current_node.children:
    #             array.append(child.name)
    #             child.depth_first_search(array, False)
    #
    #     return array


graph = Node("A")
graph.add_child("B").add_child("C").add_child("D")
graph.children[0].add_child("E").add_child("F")
graph.children[2].add_child("G").add_child("H")
graph.children[0].children[1].add_child("I").add_child("J")
graph.children[2].children[0].add_child("K")
expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
print(f"Expected:\t{expected}")
print("---------------------------------------------")
actual = graph.depth_first_search(list())
print(f"Actual:\t\t{actual}")
assert actual == expected
