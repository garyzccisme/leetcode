class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            ans = ListNode(l2.val)
            ans.next = self.mergeTwoLists(l1, l2.next)
        else:
            ans = ListNode(l1.val)
            ans.next = self.mergeTwoLists(l1.next, l2)
        return ans

# Iteration
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = ListNode()
        runner = ans

        while l1 and l2:
            if l1.val > l2.val:
                runner.next = ListNode(l2.val)
                l2 = l2.next
            else:
                runner.next = ListNode(l1.val)
                l1 = l1.next
            runner = runner.next

        runner.next = l1 or l2
        return ans.next