def foo(bar, lst):
    return lst + [bar]

some_list = []
now_list = foo('baz', some_list) #pure, the function only change its parameters

print(some_list)