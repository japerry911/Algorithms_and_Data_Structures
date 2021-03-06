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
    current = linked_list
    values_dictionary = dict()

    return_linked_list_array = list()
    return_linked_list = LinkedList(current.value)
    values_dictionary[current.value] = True

    while current.next is not None:
        current = current.next
        if current.value not in values_dictionary:
            values_dictionary[current.value] = True
            return_linked_list_array.append(current.value)

    return return_linked_list.add_many(return_linked_list_array)


test = LinkedList(1).add_many([1, 3, 4, 4, 4, 5, 6, 6])
expected = LinkedList(1).add_many([3, 4, 5, 6])
actual = remove_duplicates_from_linked_list(test)
print(actual.get_nodes_in_array(), "==", expected.get_nodes_in_array())
assert actual.get_nodes_in_array() == expected.get_nodes_in_array()
