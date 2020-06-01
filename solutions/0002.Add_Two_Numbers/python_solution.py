class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = ListNode()
        run = ans
        carry = 0

        while l1 and l2:
            carry, val = divmod(l1.val + l2.val + carry, 10)
            run.next = ListNode(val)
            run = run.next
            l1 = l1.next
            l2 = l2.next

        left = l1 or l2
        while left:
            carry, val = divmod(left.val + carry, 10)
            run.next = ListNode(val)
            run = run.next
            left = left.next

        if carry:
            run.next = ListNode(carry)

        return ans.next