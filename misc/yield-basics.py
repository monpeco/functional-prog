#the code on the generator is evaluated when the iterator require the value

def createGenerator():
    mylist = range(4)
    for i in mylist:
        print("--> %d" % i)
        yield i*i
        
mygenerator = createGenerator() 

for i in mygenerator:
    print(i)    
""" output
--> 0
0
--> 1
1
--> 2
4
--> 3
9
"""