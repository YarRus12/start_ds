def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция '{func.__name__}' вызвана {wrapper.calls} раз.")
        return func(*args, **kwargs), wrapper.calls

    wrapper.calls = 0
    return wrapper
