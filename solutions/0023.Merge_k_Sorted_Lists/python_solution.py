# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]
        return self.mergeTwoLists(self.mergeKLists(left), self.mergeKLists(right))

    def mergeTwoLists(self, l1, l2):
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
