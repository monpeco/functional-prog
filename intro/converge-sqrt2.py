#Why Functional Programming Matters by John Hughes
#http://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf

#Newton-Raphson algorithm

def next_(n, x):
    return (x+n/x)/2

print(next_(1,6))
#3

n= 2
f= lambda x: next_(n, x)
a0= 1.0
result = [ round(x,4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))),) ]
print(result)
#[1.0, 1.5, 1.4167, 1.4142]
