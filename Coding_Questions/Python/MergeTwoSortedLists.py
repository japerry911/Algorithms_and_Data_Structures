class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode or None, l2: ListNode or None) -> ListNode:
    sorted_solution = ListNode()
    sorted_solution_tmp = sorted_solution

    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    while True:
        if l1.val < l2.val:
            sorted_solution_tmp.val = l1.val
            l1 = l1.next
        else:
            sorted_solution_tmp.val = l2.val
            l2 = l2.next

        if l1 is None:
            sorted_solution_tmp.next = l2
            return sorted_solution
        elif l2 is None:
            sorted_solution_tmp.next = l1
            return sorted_solution

        sorted_solution_tmp.next = ListNode()
        sorted_solution_tmp = sorted_solution_tmp.next
