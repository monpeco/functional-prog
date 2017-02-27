year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003,
30.66),(2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
(2008, 32.84), (2009, 33.02), (2010, 32.92)]

#find the maximun key
print("find the maximun key")
print(max(year_cheese))

#find the maximun value in the position 1
print("find the maximun value in the position 1")
print(max(year_cheese, key=lambda yc: yc[1]))