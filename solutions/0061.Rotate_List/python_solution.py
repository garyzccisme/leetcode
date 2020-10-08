class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return

        runner = head
        length = 1
        while runner.next:
            runner = runner.next
            length += 1
        # KEY: put the tail back to head so that the list becomes a circle.
        runner.next = head

        for i in range(length - k % length - 1):
            head = head.next

        # Cut the circle list at `head`.
        ans, head.next = head.next, None
        return ans