#This is an generator
mygenerator = (x*x for x in range(4))
for i in mygenerator:
    print(i)
    
""" output
0
1
4
9
"""