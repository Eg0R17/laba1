from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node_list = ListNode(None)
        curret = head
        new_list = node_list
        while curret:
            if curret.val != val:
                new_list.next = curret
                new_list = new_list.next
            else:
                new_list.next = curret.next
            curret = curret.next
        return node_list.next

a6 = ListNode(1)
a5 = ListNode(1, a6)
a4 = ListNode(6, a5)
a3 = ListNode(4, a4)
a2 = ListNode(0, a3)
a1 = ListNode(1, a2)

s = Solution.removeElements(a1, 1)

print(s)