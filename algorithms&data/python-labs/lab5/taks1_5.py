# 1.	Создайте вектор (одномерный массив) размера Х, заполненный нулями
# 2.	Создайте вектор размера Х, заполненный единицами.
# 3.	Создайте вектор размера Х, заполненный нулями, в котором (у+2) элемент и (у+5) элементы равны Х.
# 4.	В массиве размера 20, поменяйте знак у элементов, имеющих значения между К и М.
# 5.	Напишите программу вычисления определителя матрицы (функция det)
# и решите системы линейных уравнений (функция solve) с помощью библиотеки linalg, встроенной в NumPy.

import numpy as np
from pprint import pprint

# Условие
X, y, K, M = 12, 3, 5, 12
col_1, col_2 = [3,3,3,3,3], [7,10,11,8,6]

# 1.	Создайте вектор (одномерный массив) размера Х, заполненный нулями
vector0 = np.zeros(X, dtype='int8')
pprint(f'Vecror of zeros: {vector0}', indent=4)

# 2.	Создайте вектор размера Х, заполненный единицами.
vector1 = np.ones(X, dtype='int8')
pprint(f'Vector of ones: {vector1}', indent=4)

# 3.	Создайте вектор размера Х, заполненный нулями, в котором (у+2) элемент и (у+5) элементы равны Х.
vector_x0 = np.zeros(X)
vector_x0[[y+1, y+4]] = X
pprint(f'Vector with {y+2} and {y+5} elements equal to {X}: {vector_x0}', indent=4)

# 4.	В массиве размера 20, поменяйте знак у элементов, имеющих значения между К и М.
array = np.arange(1, 21)
array[(array >= K) & (array <= M)] *= -1
pprint(f'Array with changed sign of elements between {K} and {M}: {array}', indent=4)

# 5.	Напишите программу вычисления определителя матрицы (функция det)
matrix_A = np.random.randint(0, 10, size=(3,3))
det_matrix_A = np.linalg.det(matrix_A)
pprint(f'Matrix A:\n{matrix_A}\nDeterminant of matrix A: {det_matrix_A}', indent=4)

#  и решите системы линейных уравнений (функция solve)
A = np.array([[2, 3],
              [1, -1]])

b = np.array([8, 1])

x = np.linalg.solve(A, b)

# Проверка
check_b = np.dot(A, x)

pprint(f'Solution of the system of equations Ax = b:\nA:\n{A}\nb: {b}\nx: {x}\nCheck (Ax): {check_b}', indent=4)

