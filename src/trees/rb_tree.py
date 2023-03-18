from trees.base import Node, Base


class RBNode(Node):
    def __init__(self, key=None, color=0, parent=None, left=None, right=None):
        super().__init__(key, parent, left, right)
        self.color = color

    def grandparent(self):
        if self.parent:
            return self.parent.parent
        return None

    def uncle(self):
        gp = self.grandparent()
        if not gp:
            return None
        if gp.left and self.parent == gp.left:
            return gp.right
        if gp.right and self.parent == gp.right:
            return gp.left


# red = 1, black = 0
class RBTree(Base):
    def __init__(self, arr=None):
        super().__init__()
        self.nil = RBNode()
        if arr is None:
            arr = []
        for key in arr:
            self.insert(key)

    def insert(self, key):
        if not self.root:
            self.root = RBNode(key, 0, None, self.nil, self.nil)
            return

        node = self._search(key, self.root)
        if key == node.key:
            raise KeyError(f'{key} already inserted')

        if key > node.key:
            node.right = RBNode(key, 1, node, self.nil, self.nil)
            node = node.right
        elif key < node.key:
            node.left = RBNode(key, 1, node, self.nil, self.nil)
            node = node.left

        self.__ins_repaint(node)

    def remove(self, key):
        if not self.root:
            raise IndexError('removing from an empty tree')

        node = self._search(key, self.root)
        if node.key != key:
            raise KeyError(key)

        if not node.left or not node.right:
            y = node
        else:
            y = self.next(node)

        if y.left:
            x = y.left
        else:
            x = y.right
        x.parent = y.parent
        if y.parent:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x
        if y != node:
            node.key = y.key
        if not y.color:
            self.__rm_repaint(x)

    def __ins_repaint(self, node):
        p = node.parent
        if not p:
            node.color = 0
            return
        u, g = node.uncle(), node.grandparent()
        if not p.color:
            return
        if u and u.color:
            p.color = 0
            u.color = 0
            g.color = 1
            self.__ins_repaint(g)
            return
        if p.right and p.right == node and g.left and p == g.left:
            self._rotate_to_left(p)
            node = node.left
        elif p.left and p.left == node and g.right and p == g.right:
            self._rotate_to_right(p)
            node = node.right
        p, g = node.parent, node.grandparent()
        p.color = 0
        g.color = 1
        if p.left and p.left == node and g.left and p == g.left:
            self._rotate_to_right(g)
        else:
            self._rotate_to_left(g)

    def __rm_repaint(self, node):
        while self.root and node.parent and not node.color:
            if node == node.parent.left:
                brother = node.parent.right
                if brother.color:
                    brother.color = 0
                    node.parent.color = 1
                    self._rotate_to_left(node.parent)
                    brother = node.parent.right
                if not brother.left.color and not brother.right.color:
                    brother.color = 1
                    node = node.parent
                else:
                    if not brother.right.color:
                        brother.left.color = 0
                        brother.color = 1
                        self._rotate_to_right(brother)
                        brother = node.parent.right
                    brother.color = node.parent.color
                    node.parent.color = 0
                    brother.right.color = 0
                    self._rotate_to_left(node.parent)
                    node = self.root
            elif node == node.parent.right:
                brother = node.parent.left
                if brother.color:
                    brother.color = 0
                    node.parent.color = 1
                    self._rotate_to_right(node.parent)
                    brother = node.parent.left
                if not brother.right.color and not brother.left.color:
                    brother.color = 1
                    node = node.parent
                else:
                    if not brother.left.color:
                        brother.right.color = 0
                        brother.color = 1
                        self._rotate_to_left(brother)
                        brother = node.parent.left
                    brother.color = node.parent.color
                    node.parent.color = 0
                    brother.left.color = 0
                    self._rotate_to_right(node.parent)
                    node = self.root
        node.color = 0
