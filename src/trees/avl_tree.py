from trees.base import Node, Base


class AVLNode(Node):
    def __init__(self, key, height=0, parent=None, left=None, right=None):
        super().__init__(key, parent, left, right)
        self.height = height

    def count_height(self):
        h_r = h_l = 0
        if self.right:
            h_r = self.right.height
        if self.left:
            h_l = self.left.height
        self.height = 1 + max(h_r, h_l)


class AVLTree(Base):
    def __init__(self, arr=None):
        super().__init__()
        if arr is None:
            arr = []
        for key in arr:
            self.insert(key)

    def insert(self, key):
        if not self.root:
            self.root = AVLNode(key)
            return

        node = self._search(key, self.root)
        if key == node.key:
            raise KeyError(f'{key} already inserted')

        if key > node.key:
            node.right = AVLNode(key, 0, node)
            node = node.right
        elif key < node.key:
            node.left = AVLNode(key, 0, node)
            node = node.left

        self.__balance(node)

    def remove(self, key):
        if not self.root:
            raise IndexError('removing from an empty tree')

        node = self._search(key, self.root)
        if node.key != key:
            raise KeyError(key)

        if not node.right and node.left:
            node.key = node.left.key
            node.left, node = None, node.left

        elif node.right:
            subst = self.next(node)
            if subst.right:
                subst.right.parent = subst.parent
            if subst > subst.parent:
                subst.parent.right = subst.right
            else:
                subst.parent.left = subst.right
            node.key = subst.key
            node = subst

        else:
            if node.parent:
                if node > node.parent:
                    node.parent.right = None
                else:
                    node.parent.left = None
            else:
                self.root = None

        if node:
            self.__balance(node.parent)

    def __balance(self, node):
        if not node:
            return

        left_h = right_h = 0
        if node.left:
            left_h = node.left.height
        if node.right:
            right_h = node.right.height

        if left_h > right_h + 1:
            self.__balance_left(node)
        if right_h > left_h + 1:
            self.__balance_right(node)
        node.count_height()

        self.__balance(node.parent)

    def __balance_left(self, node):
        node = node.left
        p = node.parent
        right_h = left_h = 0
        if node.right:
            right_h = node.right.height
        if node.left:
            left_h = node.left.height

        if right_h > left_h:
            self._rotate_to_left(node)
            node.count_height()
        self._rotate_to_right(p)

    def __balance_right(self, node):
        node = node.right
        p = node.parent
        right_h = left_h = 0
        if node.right:
            right_h = node.right.height
        if node.left:
            left_h = node.left.height

        if left_h > right_h:
            self._rotate_to_right(node)
            node.count_height()
        self._rotate_to_left(p)
