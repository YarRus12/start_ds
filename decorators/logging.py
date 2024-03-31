def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        arg_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        result = f"\nНеименованные аргументы {arg_str} \nИменованные аргументы {kwargs_str}"
        print(f'Аргументы функции {func.__name__}: {result}')
        result = func(*args, **kwargs)
        return result
    return wrapper