# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        node = head
        fast_node = head

        while node != None:
            node = node.next
            fast_node = fast_node.next.next
            if fast_node == None or fast_node.next == None:
                self.deleteNode(node)
                break
        return node

a6 = ListNode(7)
a6 = ListNode(6, a6)
a5 = ListNode(5, a6)
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

node = Solution().deleteMiddle(a1)

print(node.val)
node = a1
while node != None:
    print(node.val, end=' ')
    node = node.next
