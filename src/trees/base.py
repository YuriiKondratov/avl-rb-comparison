import functools


@functools.total_ordering
class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __bool__(self):
        return self.key is not None


class Base:
    def __init__(self):
        self.root = None

    def _rotate_to_left(self, node):
        right = node.right
        if node.parent:
            if node > node.parent:
                node.parent.right = right
            else:
                node.parent.left = right
        else:
            self.root = node.right
        right.parent = node.parent
        node.parent = right
        node.right = right.left
        if right.left:
            right.left.parent = node
        right.left = node

    def _rotate_to_right(self, node):
        left = node.left
        if node.parent:
            if node > node.parent:
                node.parent.right = node.left
            else:
                node.parent.left = node.left
        else:
            self.root = node.left
        left.parent = node.parent
        node.parent = left
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.right = node

    def _search(self, key, root):
        if key == root.key:
            return root
        if key > root.key:
            if root.right:
                return self._search(key, root.right)
            return root
        if key < root.key:
            if root.left:
                return self._search(key, root.left)
            return root

    def search(self, key):
        res = self._search(key, self.root)
        if res.key == key:
            return res
        return None

    @staticmethod
    def next(node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent:
            if node.parent > node:
                break
            node = node.parent
        return node.parent
