
# 6.	Напишите программу, которая создает:
# •	Одномерный массив NumPy под названием А из Х любых последовательных целых чисел от К.
# •	Двумерные массивы разной формы из массива А.
# •	Трехмерные массивы разной формы из массива А.

import numpy as np
from pprint import pprint

# Условие
X, y, K, M = 12, 3, 5, 12
col_1, col_2 = [3,3,3,3,3], [7,10,11,8,6]

# Одномерный массив NumPy под названием А из Х любых последовательных целых чисел от К.
print("Одномерный массив NumPy под названием А из Х любых последовательных целых чисел от К.")
A = np.arange(K, X + K)
print(A)

# Двумерные массивы разной формы из массива А.

def all_2d_shapes(A):
    arrays = []
    arr_size = np.size(A)
    for a in range(1, arr_size + 1):
        if arr_size % a == 0:
            b = arr_size // a
            arrays.append(A.reshape(a, b))
            if a != b:
                arrays.append(A.reshape(b, a))
    return arrays

print("Двумерные массивы разной формы из массива А.", all_2d_shapes(A))

# •	Трехмерные массивы разной формы из массива А.

def all_3d_shapes(A):
    arr_size = A.size
    arrays = []
    
    for a in range(1, arr_size+1):
        if arr_size % a == 0:
            for b in range(1, arr_size // a):
                if (arr_size // a) % b == 0:
                    c = arr_size // (a*b)
                    arrays.append(A.reshape(a, b, c))
    return arrays

print(all_3d_shapes(A))