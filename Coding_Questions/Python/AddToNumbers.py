# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        n1 = list()
        n2 = list()
        
        while l1 is not None:
            n1.append(str(l1.val))
            l1 = l1.next
            
        while l2 is not None:
            n2.append(str(l2.val))
            l2 = l2.next
                        
        n1 = int("".join(reversed(n1)))
        n2 = int("".join(reversed(n2)))
        
        rn = list(str(n1 + n2))
        
        try:
            head_node = ListNode(val=rn.pop())
        except IndexError:
            head_node = ListNode()
            
        next_node = head_node        
        for i in reversed(rn):
            next_node.next = ListNode(val=i)
            next_node = next_node.next
            
            
        return head_node
