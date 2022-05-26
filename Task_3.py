from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper_log(*args, **kwargs):
        print(func.__name__, end=' -> (')
        for i in args:
            print(i, type(i), end=', ')
        for kw in kwargs:
            print(kw, "=", kwargs[kw], type(kwargs[kw]), end=', ')
        print(") =", func(*args, **kwargs), end=' ')
        print(type(func(*args, **kwargs)))
    return wrapper_log


def print_func_name(func):
    def wrapper(*args, **kwargs):
        result = func (*args, **kwargs)
        print(func.__name__)
        return result
    return wrapper


@print_func_name
@type_logger
def calc_cube(*args, plus=0, minus=0):
    lst = []
    for i in args:
        lst.append(i ** 3 + plus - minus)
    return lst


calc_cube(3, 2, 1, plus=2, minus=1)
