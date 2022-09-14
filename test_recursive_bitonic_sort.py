import numpy as np

from recursive_bitonic_sort import bitonic_sort

def test_8():
    a = [2, 4, 3, 0, 7, 1, 5, 6]
    bitonic_sort(a)
    assert(all(a[i] <= a[i+1] for i in range(len(a) - 1)))

def test_random_1024():
    a = list(np.random.uniform(size=1024))
    bitonic_sort(a, d=0)
    assert(all(a[i] >= a[i+1] for i in range(len(a) - 1)))

def test_random_100000():
    a = list(np.random.uniform(size=100000))
    bitonic_sort(a)
    assert(all(a[i] <= a[i+1] for i in range(len(a) - 1)))
