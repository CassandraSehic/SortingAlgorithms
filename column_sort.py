import math
from multiprocessing import Pool
from recursive_bitonic_sort import bitonic_sort

def sort_columns(columns):
    # sorted_columns = []
    # with Pool(len(columns)) as p:
    #     sorted_columns = p.map(bitonic_sort, columns)
    # for i in range(len(columns)):
    #     columns[i] = sorted_columns[i]
    for column in columns:
        bitonic_sort(column)

def vector_to_columns_row_major(vector, r, c):
    return [[vector[j * c + i] for j in range(r)] for i in range(c)]

def vector_to_columns_column_major(vector, r, c):
    return [[vector[i * r + j] for j in range(r)] for i in range(c)]

def columns_to_vector_row_major(columns):
    r = len(columns)
    c = len(columns[0])
    return [columns[i][j] for j in range(c) for i in range(r)]

def columns_to_vector_column_major(columns):
    return [element for column in columns for element in column]

def transpose(columns):
    return vector_to_columns_row_major(columns_to_vector_column_major(columns), len(columns[0]), len(columns))

def untranspose(columns):
    return vector_to_columns_column_major(columns_to_vector_row_major(columns), len(columns[0]), len(columns))

def shift(columns):
    vector = [-math.inf for _ in range(math.floor(len(columns[0]) / 2))]
    vector += columns_to_vector_column_major(columns)
    vector += [math.inf for _ in range(math.ceil(len(columns[0]) / 2))]
    return vector_to_columns_column_major(vector, len(columns[0]), len(columns) + 1)

def unshift(columns):
    vector = columns_to_vector_column_major(columns)
    vector = [element for element in vector if element != -math.inf and element != math.inf]
    return vector_to_columns_column_major(vector, len(columns[0]), len(columns) - 1)

def sort(a, r, c):
    # assume len(a) == r * c and r % c == 0 and r >= 2 * (c - 1) ** 2
    columns = vector_to_columns_column_major(a, r, c)
    sort_columns(columns)
    columns = transpose(columns)
    sort_columns(columns)
    columns = untranspose(columns)
    sort_columns(columns)
    columns = shift(columns)
    sort_columns(columns)
    columns = unshift(columns)
    s = columns_to_vector_column_major(columns)
    for i in range(r * c):
        a[i] = s[i]

def column_sort(a):
    n = len(a)
    c = 4
    if n < 18 * 4:
        c = 3
    elif n < 8 * 3:
        c = 2
    elif n < 4:
        a.sort()
        return
    r = math.floor(n / c)
    tail = []
    for _ in range(r * c, n):
        max_element = max(a)
        a.remove(max_element)
        tail.append(max_element)
        tail.reverse()
    sort(a, r, c)
    for element in tail:
        a.append(element)
    return a
