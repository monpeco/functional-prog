#This is the basic use of yield

#definition of the generator
def createGenerator():
    mylist = range(4)
    for i in mylist:
        yield i*i
        
# create a generator
mygenerator = createGenerator() 
print(mygenerator) # mygenerator is an object!

#iterate
for i in mygenerator:
    print(i)
    
""" output
<generator object createGenerator at 0x7fcdbbc72af0>
0
1
4
9
"""