import time

def custom_sum(a, b):
    return a + b + 123

def time_calculations(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"result = {end-start}")
        
        return result
    return wrapper