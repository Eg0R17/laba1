
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:    
    def getDecimalValue(head: ListNode) -> int:
        value = 0
        while(head):
            value = value<<1
            value += head.val
            head = head.next
        return value

a5 = ListNode(1)
a4 = ListNode(1,a5)
a3 = ListNode(1, a4)
a2 = ListNode(0, a3)
a1 = ListNode(1, a2)
s = Solution.getDecimalValue(a1)

print(s)