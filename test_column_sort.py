# import numpy as np
# from column_sort import vector_to_columns_row_major, vector_to_columns_column_major
# from column_sort import columns_to_vector_row_major, columns_to_vector_column_major
# from column_sort import sort, column_sort

# def test_vector_to_columns_row_major():
#     columns = vector_to_columns_row_major([1, 2, 3, 4, 5, 6], 3, 2)
#     assert(columns == [[1, 3, 5], [2, 4, 6]])

# def test_vector_to_columns_column_major():
#     columns = vector_to_columns_column_major([1, 2, 3, 4, 5, 6], 3, 2)
#     assert(columns == [[1, 2, 3], [4, 5, 6]])

# def test_columns_to_vector_row_major():
#     vector = columns_to_vector_row_major([[1, 2, 3], [4, 5, 6]])
#     assert(vector == [1, 4, 2, 5, 3, 6])

# def test_columns_to_vector_column_major():
#     vector = columns_to_vector_column_major([[1, 2, 3], [4, 5, 6]])
#     assert(vector == [1, 2, 3, 4, 5, 6])

# def test_sort_8():
#     r = 4
#     c = 2
#     a = [3, 7, 0, 1, 6, 4, 5, 2]
#     sort(a, r, c)
#     print(a)
#     assert(all(a[i] <= a[i+1] for i in range(len(a) - 1)))

# def test_column_sort_100002():
#     a = list(np.random.uniform(size=100002))
#     column_sort(a)
#     assert(all(a[i] <= a[i+1] for i in range(len(a) - 1)))
