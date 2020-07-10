# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Straight Forward Recursion
class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if not head:
            return head

        # Keep running until meeting child or end
        runner = head
        while not runner.child and runner.next:
            runner = runner.next

        if not runner.child:
            return head

        # Store flattened node.next as tail
        # Replace node.next with flattened child
        tail, runner.next = self.flatten(runner.next), self.flatten(runner.child)
        runner.child = None
        runner.next.prev = runner

        # Let runner run to the end
        while runner.next:
            runner = runner.next

        # Append tail to end
        if tail:
            runner.next = tail
            runner.next.prev = runner

        return head


# DFS by Recursion
class Solution(object):

    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


# Iteration with Stack
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pointer = head
        branches = []
        while pointer:
            if pointer.child:
                if pointer.next: branches.append(pointer.next)
                pointer.next = pointer.child
                pointer.child = None
                pointer.next.prev = pointer
            elif not pointer.next and len(branches) > 0:
                pointer.next = branches.pop()
                pointer.next.prev = pointer
            pointer = pointer.next

        return head