import functools


def memo(func):
    """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper
