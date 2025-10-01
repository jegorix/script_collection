# # Первая: даны 2 строки, как определить какие элементы есть в одной и нет в другой

# a = "vsfdsdofv"
# b = "kreooierqvscx"

# result = {i for i in a if i in b}
# # for i in a:
# #     if i in b:
# #         result.add(i)
# print(result)

import random
from typing import List

# array = [random.randint(0, 100) for i in range(10)]


# def sequence(array: List[int]) -> int:
#     current = 0
#     max_value = 0
#     for num in array:
#         num = str(num)
#         current = (current + 1) if sum(int(i) for i in num) % 3 == 0 else 0
#         max_value = max(max_value, current)
#     return max_value


# print(array)
# print(sequence(array))


def can_decay(number: int) -> bool:
    for a in range(1, int(number**0.5 + 1)):
        b = number - a**2
        if b >= 0 and (b**0.5).is_integer:
            return True
    return False
