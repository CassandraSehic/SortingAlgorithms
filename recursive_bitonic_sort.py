import math

def compare_swap(a, i, j, d):
    if (d == 1 and a[i] > a[j]) or (d == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def merge(a, l, n, d):
    if n > 1:
        k = n // 2
        for i in range(l, l + k):
            compare_swap(a, i, i + k, d)
        merge(a, l, k, d)
        merge(a, l + k, k , d)

def sort(a, l, n, d):
    if n > 1:
        k = n // 2
        sort(a, l, k, 1)
        sort(a, l + k, k, 0)
        merge(a, l, n, d)

def bitonic_sort(a, d=1):
    n = len(a)
    log2_n = math.log2(n)
    ceil_log2_n = math.ceil(log2_n)
    if d:
        pad_value = math.inf
    else:
        pad_value = -math.inf
    for _ in range(n, 2 ** ceil_log2_n):
        a.append(pad_value)
    sort(a, 0, 2 ** ceil_log2_n, d)
    for _ in range(n, 2 ** ceil_log2_n):
        del a[-1]
    return a
