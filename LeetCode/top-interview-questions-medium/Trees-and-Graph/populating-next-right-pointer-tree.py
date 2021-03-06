

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def connect(self, root: 'Node') -> 'Node':
        preorder_recurr(root)
        return root

    def preorder_recurr(node):
        if not node: return
        if node.left:
            node.left.next = node.right
        if node.right:
            node.right.next = node.next.left if node.next else None
        preorder_recurr(node.left)
        preorder_recurr(node.right)

