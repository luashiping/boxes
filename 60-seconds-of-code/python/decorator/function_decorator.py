def decorator_b(func):
    print("decorator_b")
    def wrapper(*args, **kwargs):
        print("wrapper_b")
        return func(*args, **kwargs)
    return wrapper

def decorator_a(func):
    print("decorator_a")
    def wrapper():
        print("wrapper_a")
        return func()
    return wrapper

def decorator_c(func):
    print("decorator_c")
    def wrapper():
        print("wrapper_c")
        return func()
    return wrapper


@decorator_a
@decorator_b
@decorator_c
def test():
    print('over')

test()