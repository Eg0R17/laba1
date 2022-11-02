class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

a6 = ListNode(0)
a5 = ListNode(1, a6)
a4 = ListNode(1, a5)
a3 = ListNode(0, a4)
a2 = ListNode(4, a3)
a1 = ListNode(1, a2)
Solution().deleteNode(a1)

print()
