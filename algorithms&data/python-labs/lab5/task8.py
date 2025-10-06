import pandas as pd
import numpy as np
from pprint import pprint

# 10.
# Напишите программу выбора значения для определенного значения первого индекса серии
# с использованием модуля библиотеки Pandas.


arrays = [
    ['a', 'a', 'b', 'b', 'c', 'c'],
    [1, 2, 1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
s = pd.Series(np.arange(6), index=index)


values_for_b = s.loc['b']

response_10 = {
    'Series': s,
    'Values for b': values_for_b
}
pprint(response_10, indent=4, sort_dicts=False)


# 11.
# Напишите программу для выбора конкретного значения серии
# с использованием модуля библиотеки Pandas.

value_c2 = s.loc[('c', 2)]

response_11 = {
    'Series': s,
    "Value for ('c', 2)": value_c2
}
pprint(response_11, indent=4, sort_dicts=False)


# 12.
# Напишите программу, которая конвертирует структуры Series
# с иерархическими индексами в простой DataFrame,
# где второй набор индексов превращается в новые колонки.

df = s.unstack()

response_12 = {
    'Series': s,
    'DataFrame': df
}
pprint(response_12, indent=4, sort_dicts=False)