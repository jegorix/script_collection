from typing import Any, Callable

def retry(func: Callable, retries: int) -> Any:
    while True:
        if retries <= 0:
            raise Exception("Tries are ended")
        try:
            return func()
        except Exception as e:
            retries -= 1
            if retries <= 0:
                raise Exception("Tries are ended")
            print(f"Error - {e}! tries left: {retries}")




if __name__ == "__main__":
    # Тест 1. Функция без ошибок
    def always_succeed():
        return "Success"
    print(retry(always_succeed, 3))  # ожидаем "Success"

    # Тест 2. Функция, которая падает один раз
    attempts = {"count": 0}  # используем словарь для сохранения состояния
    def fail_once():
        if attempts["count"] < 1:
            attempts["count"] += 1
            raise ValueError("Temporary failure")
        return "Recovered"
    print(retry(fail_once, 3))  # ожидаем "Recovered" и вывод ошибки 1 раз

    # Тест 3. Функция, которая всегда падает
    def always_fail():
        raise RuntimeError("Always fails")
    try:
        retry(always_fail, 2)  # ожидаем Exception("Tries are ended") после 2 попыток
    except Exception as e:
        print(e)