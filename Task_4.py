def val_checker(val):
    def _val_checker(func):
        def wrapper(x):
            if val(x):
                print(func(x))
            else:
                raise ValueError(f'wrong value: {x}')

        return wrapper
    return _val_checker


@val_checker(lambda a: a > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-1)
