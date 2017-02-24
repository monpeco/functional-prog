
def within(epsilon, iterable):
    def head_tail(epsilon, a, iterable):
        b= next(iterable)
        if abs(a-b) <= epsilon: return b
        return head_tail(epsilon, b, iterable)
    return head_tail(epsilon, next(iterable), iterable)
    
 