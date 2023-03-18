from graphviz import Digraph


def rb_traversal(root, g: Digraph):
    if not root:
        return
    if root.color:
        g.node(f"{root.key}", color="red")
    else:
        g.node(f"{root.key}", color="black")
    if root.left:
        g.edge(f"{root.key}", f"{root.left.key}")
    if root.right:
        g.edge(f"{root.key}", f"{root.right.key}")
    rb_traversal(root.right, g)
    rb_traversal(root.left, g)


def visualize_rb_tree(tree):
    g = Digraph()
    rb_traversal(tree.root, g)
    g.view()


def avl_traversal(root, g: Digraph):
    if not root:
        return
    g.node(f"{root.key}", f"{root.key}, h = {root.height}")
    if root.left:
        g.edge(f"{root.key}", f"{root.left.key}")
    if root.right:
        g.edge(f"{root.key}", f"{root.right.key}")
    avl_traversal(root.right, g)
    avl_traversal(root.left, g)


def visualize_avl_tree(tree):
    g = Digraph()
    avl_traversal(tree.root, g)
    g.view()
