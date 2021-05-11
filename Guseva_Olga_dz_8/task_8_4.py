from functools import wraps

def value_cheker(exp):
    def _value_cheker(func):
        @wraps(func)
        def wrapper(*args):
            x = args[0]
            if exp(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')
        return wrapper()
    return _value_cheker()


@value_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


