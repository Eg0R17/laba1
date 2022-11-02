from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(0)
        odd = odd_head
        even_head = ListNode(0)
        even = even_head
        count = 0

        while head:
            if count % 2 == 0:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            count += 1
            head = head.next
        even.next = None
        odd.next = even_head.next

        return odd_head.next


a6 = ListNode(0)
a5 = ListNode(1, a6)
a4 = ListNode(1, a5)
a3 = ListNode(0, a4)
a2 = ListNode(4, a3)
a1 = ListNode(1, a2)
s = Solution().oddEvenList(a1)

print(s)
