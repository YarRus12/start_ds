def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        arg_str = ', '.join(repr(arg) for arg in args)
        if arg_str != '':
            print(f'Аргументы функции {func.__name__}: {arg_str}')
        else:
            print(f'Функции {func.__name__} вызвана без аргументов')
        result = func(*args, **kwargs)
        return result
    return wrapper

