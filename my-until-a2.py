def my_until(top, filtro, value):
    if value==top: return []
    if filtro(value): return [value] + my_until(top, filtro, value+1)
    else: return my_until(top, filtro, value+1)
    
result=my_until(10, lambda x: x%2==0, 0)
print(result)
