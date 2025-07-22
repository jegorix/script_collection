import time
from utils import custom_sum, time_calculations

print(custom_sum(1, 3))
# print(custom_sum("vdfdf", "vsdffds"))

@time_calculations
def default_sum(a: int, b: int, sleep: int) -> int:
    time.sleep(sleep)
    return a + b

print(default_sum(1,2,1))