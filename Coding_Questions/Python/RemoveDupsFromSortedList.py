class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode or None:
    if head is None:
        return None

    solution = ListNode(val=head.val)
    return_solution = solution
    previous_value = head.val

    while head.next is not None:
        head = head.next

        if head.val != previous_value:
            solution.next = ListNode(val=head.val)
            solution = solution.next
            previous_value = head.val

    return return_solution
