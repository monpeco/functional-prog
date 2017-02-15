def until(n, filter_func, v):
    if v == n: return []
    if filter_func(v): return [v] + until( n, filter_func, v+1 )
    else: return until(n, filter_func, v+1)
    
out = until(10, lambda x: x%3==0 or x%5==0, 0)
print(out)
# >>> [0, 3, 5, 6, 9]   

