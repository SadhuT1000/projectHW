from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Декоратор Логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"

                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
                print(log_message)

            except Exception as e:

                log_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"

                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
                print(log_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
