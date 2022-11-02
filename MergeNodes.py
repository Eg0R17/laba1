from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_list = None
        new_listNode = None
        sum=0
        while node != None:
            if node.val!=0:
                sum+=node.val
            else:
                if new_list == None:
                    new_list=ListNode(sum)
                    new_listNode=new_list
                else:
                    new_listNode.next = ListNode(sum)
                    new_listNode=new_listNode.next
                sum=0
            node = node.next
        return new_list

a6 = ListNode(0)
a5 = ListNode(1, a6)
a4 = ListNode(1, a5)
a3 = ListNode(0, a4)
a2 = ListNode(4, a3)
a1 = ListNode(1, a2)
s = Solution.mergeNodes(a1)

print(s)





