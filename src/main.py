from instruments.plotting import make_plot
from trees.avl_tree import AVLTree
from trees.rb_tree import RBTree
from instruments.generator import *
from instruments.visual import *


def main():
    opt1 = input("Please enter 'v' if you want visualizing and 'p' if you want some plots:")
    if opt1 == 'v':
        t_type = input("Choose you hero!!! (Enter 'avl' for AVL or 'rb' for RB):")
        data = [int(x) for x in input("Please enter key values seperated by spaces:\n").split()]
        if t_type == 'avl':
            tree = AVLTree(data)
            visualize_avl_tree(tree)
        elif t_type == 'rb':
            tree = RBTree(data)
            visualize_rb_tree(tree)
        else:
            raise Exception("unknown tree type")
    elif opt1 == 'p':
        gen = input("Choose data generation way ('r' for random, 's' for sorted):")
        opt = input("Enter operation ('i' for insertion, 's' for search, 'r' for remove):")
        n = int(input("Enter number of elements:"))
        t_n = int(input("Enter number of tests:"))
        name = input("Enter filename:")
        print("Processing...")
        if gen == 'r':
            make_plot(opt, n, t_n, name, pseudo_random_generator)
        elif gen == 's':
            make_plot(opt, n, t_n, name, sorted_generator)

    else:
        raise Exception("unknown operation")


if __name__ == "__main__":
    main()
