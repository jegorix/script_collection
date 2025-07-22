from typing import Callable, TypeVar

T = TypeVar("T")

def custom_sum(a: int, b: int) -> int: ...

def time_calculations(func: Callable[..., T]) -> Callable[..., T]: ...