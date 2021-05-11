
def my_generate (n):
    for i in range(1,n+1,2):
        yield i

result = my_generate(11)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))


