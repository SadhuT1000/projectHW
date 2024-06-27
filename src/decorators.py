from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор Логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

            except Exception as e:

                log_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
