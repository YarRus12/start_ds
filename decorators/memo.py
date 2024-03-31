from functools import wraps
import typing


def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
    """

    @wraps(func)
    def fmemo(*args):
        if all(isinstance(arg, typing.Hashable) for arg in args):
            if args in fmemo.cache:
                result = fmemo.cache[args]
            else:
                result = fmemo.cache[args] = func(*args)
            return result
        else:
            return func(*args)

    fmemo.cache = {}
    return fmemo
