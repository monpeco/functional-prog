some_list = []

def foo(bar):
    some_list.append(bar)   #impure, change a value that is not a parameter

foo('baz')

print(some_list)