from typing import List


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def add_many(self, values: List[int]):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def get_nodes_in_array(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def remove_duplicates_from_linked_list(linked_list: LinkedList) -> LinkedList:
    return linked_list


test = LinkedList(1).add_many([1, 3, 4, 4, 4, 5, 6, 6])
expected = LinkedList(1).add_many([3, 4, 5, 6])
actual = remove_duplicates_from_linked_list(test)
print(actual.get_nodes_in_array(), "==", expected.get_nodes_in_array())
assert actual.get_nodes_in_array() == expected.get_nodes_in_array()
