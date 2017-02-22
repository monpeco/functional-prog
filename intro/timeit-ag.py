import timeit

print("timeit.timeit('((([]+[1])+[2])+[3])+[4]') %f" % timeit.timeit("((([]+[1])+[2])+[3])+[4]"))
print("timeit.timeit('[]+([1]+([2]+([3]+[4])))') %f" % timeit.timeit("[]+([1]+([2]+([3]+[4])))"))

