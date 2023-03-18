import numpy as np
from random import shuffle
import time


def multiple_time_measuring(data, func):
    if type(data) != list:
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        return end - start

    times = []
    for value in data:
        start = time.perf_counter()
        func(value)
        end = time.perf_counter()
        times.append(end - start)
    return times


def tree_insert_measure(tests_num, elements_num, generator, tree_class):
    times = np.zeros(elements_num)
    for _ in range(tests_num):
        data = generator(0, elements_num)
        tree = tree_class()
        times += np.array(multiple_time_measuring(data, tree.insert))
    times /= tests_num
    return times


def tree_remove_measure(tests_num, elements_num, generator, tree_class):
    times = np.zeros(elements_num)
    for _ in range(tests_num):
        data = generator(0, elements_num)
        tree = tree_class(data)
        times += np.array(multiple_time_measuring(data, tree.remove))
    times /= tests_num
    times = times[::-1]
    return times


def tree_search_measure(tests_num, elements_num, generator, tree_class):
    times = np.zeros(elements_num)
    for _ in range(tests_num):
        data = generator(0, elements_num)
        tree = tree_class(data)
        shuffle(data)
        for i, value in enumerate(data):
            times[i] += multiple_time_measuring(value, tree.search)
            tree.remove(data[i])
    times /= tests_num
    times = times[::-1]
    return times
