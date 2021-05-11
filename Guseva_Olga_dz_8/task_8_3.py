def args_type(func):
    def logger(*args, **kwargs):
        for arg in args:
            print(f'{str(arg)}: {type(arg)}')
        for key, value in kwargs.items():
            print(f'{key}={str(value)}: {type(value)}')
    return logger()


@args_type
def num_cubs(*args, **kwargs):
    result_list = []
    for num in args:
        result_list.append(num ** 3)



num_cubs(1, 2, 3, 4)