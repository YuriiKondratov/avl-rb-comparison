from instruments.time_measuring import *
import matplotlib.pyplot as plt
from trees.avl_tree import AVLTree
from trees.rb_tree import RBTree


def make_plot(opt, n, t_n, plt_name, gen):
    scale = 10 ** 6

    generator = gen
    y_1 = y_2 = []

    if opt == 'i':
        y_1 = [scale * y for y in tree_insert_measure(t_n, n, generator, RBTree)]
        y_2 = [scale * y for y in tree_insert_measure(t_n, n, generator, AVLTree)]
    elif opt == 'r':
        y_1 = [scale * y for y in tree_remove_measure(t_n, n, generator, RBTree)]
        y_2 = [scale * y for y in tree_remove_measure(t_n, n, generator, AVLTree)]
    elif opt == 's':
        y_1 = [scale * y for y in tree_search_measure(t_n, n, generator, RBTree)]
        y_2 = [scale * y for y in tree_search_measure(t_n, n, generator, AVLTree)]
    else:
        raise AttributeError("unknown operation")

    plt.plot(list(range(n)), y_1, 'ro', list(range(n)), y_2, 'go', markersize='0.5')
    plt.ylim(0, int((sum(y_1) + sum(y_2)) / n))
    plt.xlabel('n')
    plt.ylabel('time, μs')
    plt.legend(['rb', 'avl'])
    plt.savefig(plt_name + '.png')
