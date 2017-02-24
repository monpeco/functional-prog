
def within(epsilon, iterable):
    def head_tail(epsilon, a, iterable):
        b= next(iterable)
        if abs(a-b) <= epsilon: return b
        return head_tail(epsilon, b, iterable)
    return head_tail(epsilon, next(iterable), iterable)
    
def next_(n, x):
    return (x+n/x)/2
    
def sqrt(a0, epsilon, n):
    return within(epsilon, repeat(lambda x: next_(n,x))) #problem repeat

sqrt(4, 0.1, 2) #not working