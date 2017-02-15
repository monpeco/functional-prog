def my_until(top, filtro, value):
    if value==top: return []
    if filtro(value): return [value] + my_until(top, filtro, value+1)
    else: return my_until(top, filtro, value+1)

def sum(p_list):
    if len(p_list) == 0: return 0
    return p_list[0] + sum(p_list[1:])
    
result=my_until(10, lambda x: x%2==0, 0)
print("Sequence: %s" % result)
sum_result = sum(result)
print("Sum: %s" % sum_result)
